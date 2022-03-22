import argparse
import json
import os
from fnmatch import fnmatch
from os.path import exists
from pathlib import Path
from typing import List

import boto3
from pick import pick

template_root = f"{str(Path(__file__).parent)}/events/"
registry_name = "lambda-testevent-schemas"


def get_main_args_parser() -> argparse.ArgumentParser:
    """Build the cli argument parser"""
    parser = argparse.ArgumentParser(prog="publish-shared-event", description="List the content of a folder")
    parser.add_argument("-r", dest="region", help="Set AWS Region")
    parser.add_argument("-f", dest="lambda_name", help="Name of the lambda function")
    parser.add_argument("-e", dest="event_source", help="Event source")
    parser.add_argument("--list", help="List of supported event sources", action="store_true")
    parser.add_argument("--filtered-list", help="Filtered list")
    return parser


def list_of_test_events() -> List[str]:
    """Get the list of supported test events"""
    templates = []
    for path, _, files in os.walk(template_root):
        templates.extend(
            os.path.join(path, name).removeprefix(template_root) for name in files if fnmatch(name, "*.json")
        )
    templates.sort()
    return templates


def get_lambda_name(session: boto3.session.Session) -> str:
    """Prompt to select which lambda event to add a shareable test event."""
    lambda_client = session.client("lambda")
    response = lambda_client.list_functions()
    functions = [f["FunctionName"] for f in response["Functions"]]
    return pick(functions, "Select Lambda function:")[0]


def get_test_event(list_of_events: List[str]) -> str:
    """Prompt to select which test event to use"""
    return pick(list_of_events, "Select Event:")[0]


def create_registry_if_not_exists(schemas_client):
    """Create the event bridge registry for shareable test events"""
    try:
        schemas_client.describe_registry(RegistryName=registry_name)
    except schemas_client.exceptions.NotFoundException:
        print("Registry not found, creating...")
        schemas_client.create_registry(
            RegistryName=registry_name,
            Description="List of shareable tests events for AWS Lambda",
            Tags={
                "comment": "List of shareable tests events for AWS Lambda",
            },
        )


def create_or_update_schema(schemas_client, lambda_name: str, test_event: str):
    """Create or update shareable test event for the specified lambda_name"""
    content = generate_schema(test_event)
    try:
        schemas_client.create_schema(
            RegistryName="lambda-testevent-schemas",
            SchemaName=f"_{lambda_name}-schema",
            Content=content,
            Type="JSONSchemaDraft4",
            Description="Sample sharable event",
            Tags={"comment": "Sample sharable event"},
        )
    except schemas_client.exceptions.ConflictException:
        print("Schema already exists, updating...")
        schemas_client.update_schema(
            RegistryName="lambda-testevent-schemas",
            SchemaName=f"_{lambda_name}-schema",
            Content=content,
            Type="JSONSchemaDraft4",
        )


def generate_schema(test_event: str) -> str:
    """Generates an event bridge schema from the test event file"""
    if exists(test_event):
        path = Path(test_event)
    else:
        path = Path(template_root + test_event)
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


def main():
    args_parser = get_main_args_parser()
    args = args_parser.parse_args()
    list_of_events = list_of_test_events()

    if args.list:
        print("List of supported event sources:")
        print(*list_of_events, sep="\n")
        return
    if args.filtered_list:
        filtered_list = list(filter(lambda x: x.startswith(args.filtered_list), list_of_events))
        print("Filtered list of supported event sources:")
        print(*filtered_list, sep="\n")
        return

    session = boto3.session.Session(region_name=args.region)
    lambda_name = args.lambda_name or get_lambda_name(session)
    test_event = args.event_source or get_test_event(list_of_events)
    schemas_client = session.client("schemas")

    create_registry_if_not_exists(schemas_client)
    create_or_update_schema(schemas_client, lambda_name, test_event)


if __name__ == "__main__":
    main()
