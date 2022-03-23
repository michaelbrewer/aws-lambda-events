import argparse
import json
import os
import sys
from fnmatch import fnmatch
from os.path import exists
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import boto3
from pick import pick

template_root = f"{str(Path(__file__).parent)}/events/"
registry_name = "lambda-testevent-schemas"


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse arguments from the cli"""
    parser = argparse.ArgumentParser(prog="publish-shared-event", description="List the content of a folder")
    parser.add_argument("-r", dest="region", help="Set AWS Region")
    parser.add_argument("-f", dest="lambda_name", help="Name of the lambda function")
    parser.add_argument("-e", dest="event_source", help="Event source")
    parser.add_argument("--list", help="List of supported event sources", action="store_true")
    parser.add_argument("--filtered-list", help="Filtered list")
    parser.add_argument("-n", dest="example_name", help="Set the example name")
    return parser.parse_args(args)


def list_of_test_events() -> List[str]:
    """Get the list of supported test events"""
    templates = []
    for path, _, files in os.walk(template_root):
        templates.extend(
            os.path.join(path, name).removeprefix(template_root) for name in files if fnmatch(name, "*.json")
        )
    templates.sort()
    return templates


def get_session(region: Optional[str]) -> boto3.session.Session:
    return boto3.session.Session(region_name=region)


def get_lambda_name(session: boto3.session.Session) -> str:
    """Prompt to select which lambda event to add a shareable test event."""
    lambda_client = session.client("lambda")
    response = lambda_client.list_functions()
    if functions := [f["FunctionName"] for f in response["Functions"]]:
        return pick(functions, f"Select Lambda function ({session.region_name}):")[0]
    print(f"No lambdas exist yet in this region: {session.region_name}")
    return input("Lambda function name:")


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


def create_or_update_schema(schemas_client, lambda_name: str, test_event: str, example_name: Optional[str]):
    """Create or update shareable test event for the specified lambda_name"""
    schema_name = f"_{lambda_name}-schema"
    example_name, event = build_test_event(test_event, example_name)
    try:
        existing_schema = schemas_client.describe_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
        )
        content = generate_updated_schema_content(json.loads(existing_schema["Content"]), example_name, event)
        print(f"Schema '{schema_name}' already exists, updating...")
        schemas_client.update_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
            Content=content,
            Type="JSONSchemaDraft4",
        )

    except schemas_client.exceptions.NotFoundException:
        content = generate_new_schema_content(example_name, event)
        schemas_client.create_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
            Content=content,
            Type="JSONSchemaDraft4",
            Description="Lambda sharable test event",
        )


def build_test_event(test_event: str, example_name: Optional[str]) -> Tuple[str, Dict]:
    path = get_test_event_path(test_event)
    example_name = example_name or path.name.replace(".json", "")
    event = json.loads(path.read_text())
    return example_name, event


def get_test_event_path(test_event: str) -> Path:
    if exists(test_event):  # Allows for locally defined test events
        return Path(test_event)
    else:  # One of the standard test events
        return Path(template_root + test_event)


def generate_updated_schema_content(schema: Dict, example_name: str, event: Dict) -> str:
    """Appends or updates the existing schema examples"""
    schema["components"]["examples"][example_name] = {"value": event}
    return json.dumps(schema)


def generate_new_schema_content(example_name: str, event: Dict) -> str:
    """Generates an event bridge schema from the test event file"""
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
    args = parse_args(sys.argv[1:])
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

    session = get_session(args.region)
    lambda_name = args.lambda_name or get_lambda_name(session)
    test_event = args.event_source or get_test_event(list_of_events)

    schemas_client = session.client("schemas")
    create_registry_if_not_exists(schemas_client)
    create_or_update_schema(schemas_client, lambda_name, test_event, args.example_name)


if __name__ == "__main__":
    main()
