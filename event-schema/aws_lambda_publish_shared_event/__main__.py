import argparse
import json
import sys
from typing import Dict, List, Optional

import boto3
from pick import pick

from aws_lambda_publish_shared_event.util import build_test_event, handle_list_arguments, list_of_test_events

registry_name = "lambda-testevent-schemas"


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse arguments from the cli"""
    parser = argparse.ArgumentParser(prog="publish-shared-event", description="List the content of a folder")
    parser.add_argument("-r", "-region", dest="region", help="Set AWS Region")
    parser.add_argument("-f", "--lambda-name", dest="lambda_name", help="Name of the Lambda function")
    parser.add_argument("-e", "--event", dest="event", help="Event source")
    parser.add_argument("-n", "--event-name", dest="event_name", help="Event name")
    parser.add_argument("-l", "--list", dest="list", help="List of supported event sources", action="store_true")
    parser.add_argument("--filtered-list", dest="filtered_list", help="Filtered list")
    return parser.parse_args(args)


def get_session(region: Optional[str]) -> boto3.session.Session:
    return boto3.session.Session(region_name=region)


def get_lambda_name(session: boto3.session.Session) -> str:
    """Prompt to select which Lambda event to add a shareable test event."""
    lambda_client = session.client("lambda")
    response = lambda_client.list_functions()
    # sourcery skip: use-named-expression
    # as we support python 3.7
    functions = [f["FunctionName"] for f in response["Functions"]]
    if functions:
        return pick(functions, f"Select Lambda function ({session.region_name}): ")[0][0]
    print(f"No lambdas exist yet in this region: {session.region_name}")
    return input("Lambda function name: ")


def get_test_event(list_of_events: List[str]) -> str:
    """Prompt to select which test event to use"""
    return pick(list_of_events, "Select Event: ")[0][0]


def create_registry(schemas_client):
    """Create the event bridge registry for shareable test events"""
    try:
        schemas_client.create_registry(
            RegistryName=registry_name,
            Description="List of shareable tests events for AWS Lambda",
        )
    except schemas_client.exceptions.ConflictException:
        print(f"Registry with name '{registry_name}' already exists.")


def update_schema(schemas_client, lambda_name: str, event_path: str, event_name: Optional[str]):
    """Create or update shareable test event for the specified lambda_name"""
    schema_name = f"_{lambda_name}-schema"
    name, event = build_test_event(event_name, event_path)
    try:
        existing_schema = schemas_client.describe_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
        )
        content = generate_updated_schema_content(json.loads(existing_schema["Content"]), name, event)
        print(f"Schema '{schema_name}' already exists, updating...")
        schemas_client.update_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
            Content=content,
            Type="JSONSchemaDraft4",
        )

    except schemas_client.exceptions.NotFoundException:
        content = generate_new_schema_content(name, event)
        schemas_client.create_schema(
            RegistryName=registry_name,
            SchemaName=schema_name,
            Content=content,
            Type="JSONSchemaDraft4",
            Description="Lambda sharable test event",
        )


def generate_updated_schema_content(schema: Dict, event_name: str, event: Dict) -> str:
    """Updates or appends to the existing schema examples"""
    schema["components"]["examples"][event_name] = {"value": event}
    return json.dumps(schema)


def generate_new_schema_content(event_name: str, event: Dict) -> str:
    """Generates an event bridge schema from the test event file"""
    schema = {
        "openapi": "3.0.0",
        "info": {
            "version": "1.0.0",
            "title": "Event",
        },
        "paths": {},
        "components": {
            # Could also include a collection of JSONSchemaDraft4
            # something like: "schemas" : { "Event": build_json_schema(event) },
            "examples": {
                event_name: {
                    "value": event,
                }
            },
        },
    }
    return json.dumps(schema)


def main():
    args = parse_args(sys.argv[1:])
    if handle_list_arguments(args):
        return

    session = get_session(args.region)
    lambda_name = args.lambda_name or get_lambda_name(session)
    event_path = args.event or get_test_event(list_of_test_events())
    schemas_client = session.client("schemas")
    create_registry(schemas_client)
    update_schema(schemas_client, lambda_name, event_path, args.event_name)


if __name__ == "__main__":
    main()
