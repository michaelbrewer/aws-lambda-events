import argparse
import json
import os
from fnmatch import fnmatch
from pathlib import Path
from typing import List

import boto3
from pick import pick

template_root = str(Path(__file__).parent.parent.parent) + "/docs/events/"
registry_name = "lambda-testevent-schemas"


def main():
    args_parser = argparse.ArgumentParser(prog="publish-shared-event", description="List the content of a folder")
    args_parser.add_argument("-r", dest="region", help="Set AWS Region")
    args_parser.add_argument("-f", dest="lambda_name", help="Name of the lambda function")
    args_parser.add_argument("-e", dest="event_source", help="Event source")
    args_parser.add_argument("--list", help="List of supported event sources", action="store_true")
    args_parser.add_argument("--filtered-list", help="Filtered list")
    args = args_parser.parse_args()

    if args.list:
        print("List of supported event sources:")
        print(*get_list_of_events(), sep="\n")
        return
    if args.filtered_list:
        filtered_list = list(filter(lambda x: x.startswith(args.filtered_list), get_list_of_events()))
        print("Filtered list of supported event sources:")
        print(*filtered_list, sep="\n")
        return

    lambda_name = args.lambda_name or input("Lambda Name: ")
    if args.event_source:
        event_source = args.event_source
    else:
        event_source, _ = pick(get_list_of_events(), "Select Event:")

    client = boto3.client("schemas", region_name=args.region)
    create_registry_if_not_exists(client)
    client.create_schema(
        RegistryName="lambda-testevent-schemas",
        SchemaName=f"_{lambda_name}-schema",
        Content=generate_schema(event_source),
        Description="Sample sharable event",
        Tags={"comment": "Sample sharable event"},
        Type="JSONSchemaDraft4",
    )


def create_registry_if_not_exists(client):
    try:
        client.describe_registry(RegistryName=registry_name)
    except client.exceptions.NotFoundException:
        print("Registry not found, creating...")
        client.create_registry(
            RegistryName=registry_name,
            Description="List of shareable tests events for AWS Lambda",
            Tags={
                "comment": "List of shareable tests events for AWS Lambda",
            },
        )


def get_list_of_events() -> List[str]:
    templates = []
    for path, _, files in os.walk(template_root):
        for name in files:
            if fnmatch(name, "*.json"):
                templates.append(os.path.join(path, name).removeprefix(template_root))
    templates.sort()
    return templates


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


if __name__ == "__main__":
    main()
