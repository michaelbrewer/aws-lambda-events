import json
from pathlib import Path

import boto3


def load_event_schema(path: Path) -> str:
    return json.loads(path.read_text())


def generate_schema(example_file: str) -> str:
    path = Path(str(Path(__file__).parent.parent.parent) + "/docs/events/" + example_file)
    example_name = path.name.replace(".json", "")
    event = load_event_schema(path)
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


lambda_name = input("Lambda Name: ")
event_source = input("Event Source: ")

client = boto3.client("schemas")
client.create_schema(
    RegistryName="lambda-testevent-schemas",
    SchemaName=f"_{lambda_name}-schema",
    Content=generate_schema(event_source),
    Description="Sample sharable event",
    Tags={"comment": "Sample sharable event"},
    Type="JSONSchemaDraft4",
)
