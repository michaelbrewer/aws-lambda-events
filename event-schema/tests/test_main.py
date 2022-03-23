import json
import sys
from unittest import mock

import pytest

from src.aws_lambda_publish_shared_event.__main__ import generate_new_schema_content, main

SCRIPT_NAME = "foo.py"


def test_parse_args_help(capsys):
    sys.argv = [SCRIPT_NAME, "--help"]
    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert captured.out.startswith("usage:")


def test_parse_args_list(capsys):
    sys.argv = [SCRIPT_NAME, "--list"]

    main()

    captured = capsys.readouterr()
    assert captured.out.startswith("List of supported event sources:")


def test_parse_args_filtered(capsys):
    sys.argv = [SCRIPT_NAME, "--filtered-list", "ses/"]

    main()

    captured = capsys.readouterr()
    assert captured.out.startswith("Filtered list of supported event sources:")


def test_generate_updated_schema_content():
    sys.argv = [SCRIPT_NAME, "-e", "ses/ses.json", "-f", "name", "-r", "us-east-1"]
    with mock.patch("src.aws_lambda_publish_shared_event.__main__.get_session") as mock_boto3:
        client = mock_boto3.return_value.client
        client.return_value.describe_schema.return_value = {"Content": '{"components": {"examples": {}}}'}

        main()

        client.assert_called_with("schemas")
        client.return_value.describe_registry.assert_called_with(RegistryName="lambda-testevent-schemas")
        client.return_value.describe_schema.assert_called_with(
            RegistryName="lambda-testevent-schemas",
            SchemaName="_name-schema",
        )
        client.return_value.update_schema.assert_called()


def test_generate_new_schema_content():
    example_name = "foo"
    event = {"message": "Foo"}
    expected = {
        "openapi": "3.0.0",
        "info": {"version": "1.0.0", "title": "Event"},
        "components": {
            "examples": {
                example_name: {"value": event},
            },
        },
    }

    assert generate_new_schema_content(example_name, event) == json.dumps(expected)
