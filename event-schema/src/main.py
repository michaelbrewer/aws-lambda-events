import json
from pathlib import Path

import boto3


def load_event_schema(event_schema: str) -> str:
    path = Path(str(Path(__file__).parent) + "/" + event_schema + ".json")
    return json.dumps(json.loads(path.read_text()))


lambda_name = input("Lambda Name: ")
event_source = input("Event Source: ")

client = boto3.client("schemas")
client.create_schema(
    RegistryName="lambda-testevent-schemas",
    SchemaName="_" + lambda_name + "-schema",
    Content=load_event_schema(event_source),
    Description="Sample sharable event",
    Tags={"comment": "Sample sharable event"},
    Type="JSONSchemaDraft4",
)
