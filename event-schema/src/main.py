import json
import os
from fnmatch import fnmatch
from pathlib import Path

import boto3
from pick import pick

template_root = str(Path(__file__).parent.parent.parent) + "/docs/events/"


def generate_schema(example_file: str) -> str:
    path = Path(template_root + example_file)
    example_name = path.name.replace(".json", "")
    event = json.loads(path.read_text())
    schema = {
        "openapi": "3.0.0",
        "info": {
            "version": "1.0.0",
            "title": "Event",
        },
        "components": {
            "examples": {
                example_name: {
                    "value": event,
                }
            },
        },
    }
    return json.dumps(schema)


def get_list_of_events() -> list:
    templates = []
    for path, _, files in os.walk(template_root):
        for name in files:
            if fnmatch(name, "*.json"):
                templates.append(os.path.join(path, name).removeprefix(template_root))
    templates.sort()
    return templates


lambda_name = input("Lambda Name: ")
title = "Select Event:"
event_source, index = pick(get_list_of_events(), title)

client = boto3.client("schemas")
client.create_schema(
    RegistryName="lambda-testevent-schemas",
    SchemaName=f"_{lambda_name}-schema",
    Content=generate_schema(event_source),
    Description="Sample sharable event",
    Tags={"comment": "Sample sharable event"},
    Type="JSONSchemaDraft4",
)
