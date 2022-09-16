import importlib
import json
import sys
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

import boto3
import pytest
from botocore.stub import Stubber

from aws_lambda_publish_shared_event import __main__, util

SCRIPT_NAME = "foo.py"
AWS_REGION = "us-east-1"


@pytest.mark.parametrize("argument", ["-h", "--help"])
def test_parse_args_help(capsys, argument: str):
    # GIVEN
    sys.argv = [SCRIPT_NAME, argument]

    # WHEN
    with pytest.raises(SystemExit):
        __main__.main()

    # THEN
    captured = capsys.readouterr()
    assert captured.out.startswith("usage:")


@pytest.mark.parametrize("argument", ["-l", "--list"])
def test_parse_args_list(capsys, argument: str):
    # GIVEN
    sys.argv = [SCRIPT_NAME, argument]

    # WHEN
    __main__.main()

    # THEN
    captured = capsys.readouterr()
    assert captured.out.startswith("List of supported event sources:")


def test_parse_args_filtered(capsys):
    sys.argv = [SCRIPT_NAME, "--filtered-list", "ses/"]

    __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("Filtered list of supported event sources:")


def test_generate_updated_schema_content():
    function_name = "hello-world"
    sys.argv = [SCRIPT_NAME, "-e", "ses/ses.json", "-f", function_name, "-r", "us-east-1"]
    with mock.patch("aws_lambda_publish_shared_event.__main__.get_session") as mock_boto3:
        client = mock_boto3.return_value.client
        client.return_value.describe_schema.return_value = {"Content": '{"components": {"examples": {}}}'}

        __main__.main()

        client.assert_called_with("schemas")
        client.return_value.create_registry.assert_called_with(
            RegistryName="lambda-testevent-schemas",
            Description="List of shareable tests events for AWS Lambda",
        )
        client.return_value.describe_schema.assert_called_with(
            RegistryName="lambda-testevent-schemas",
            SchemaName=f"_{function_name}-schema",
        )
        client.return_value.update_schema.assert_called()


def test_generate_new_schema_content():
    example_name = "foo"
    event = {"message": "Foo"}
    expected = {
        "openapi": "3.0.0",
        "info": {"version": "1.0.0", "title": "Event"},
        "paths": {},
        "components": {
            "examples": {
                example_name: {"value": event},
            },
        },
    }

    assert __main__.generate_new_schema_content(example_name, event) == json.dumps(expected)


def test_get_session():
    assert __main__.get_session("us-east-1") is not None


@mock.patch("pick.pick")
def test_get_test_event(mock_pick: MagicMock):
    importlib.reload(__main__)

    __main__.get_test_event(["one"])

    mock_pick.assert_called()


def test_get_lambda_name():
    expected = "foo"

    def mock_input(_):
        return expected

    __main__.input = mock_input

    with mock.patch("boto3.session.Session") as mock_session:
        assert __main__.get_lambda_name(mock_session) == expected
        mock_session.client.assert_called_with("lambda")
        mock_session.client.return_value.list_functions.assert_called()


@mock.patch("pick.pick")
def test_get_lambda_name_list(mock_pick: MagicMock):
    importlib.reload(__main__)

    with mock.patch("boto3.session.Session") as mock_session:
        mock_session.client.return_value.list_functions.return_value = {"Functions": [{"FunctionName": "name"}]}
        assert __main__.get_lambda_name(mock_session) is not None

    mock_pick.assert_called()


def test_get_test_event_path():
    expected = Path(__file__).parent / "test.json"
    assert util.get_test_event_path(str(expected)) == expected


def test_create_registry_if_not_exists_already_exist():
    schemas_client = boto3.client("schemas", region_name=AWS_REGION)
    stubber = Stubber(schemas_client)
    stubber.add_client_error(
        method="create_registry",
        service_error_code="ConflictException",
        service_message="Already exists",
        http_status_code=400,
    )
    stubber.activate()

    __main__.create_registry(schemas_client)


def test_create_or_update_schema_not_found():
    schemas_client = boto3.client("schemas", region_name=AWS_REGION)
    stubber = Stubber(schemas_client)
    stubber.add_client_error(
        method="describe_schema",
        service_error_code="NotFoundException",
        service_message="Not found",
        http_status_code=400,
    )
    stubber.add_response("create_schema", {})
    stubber.activate()

    __main__.update_schema(schemas_client, "foo", "ses/ses.json", "ses")


def test_show_version_number(capsys):
    sys.argv = [SCRIPT_NAME, "--version"]

    __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("0.18.0")
