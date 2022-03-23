import importlib
import json
import sys
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

import pytest

from aws_lambda_publish_shared_event import __main__

SCRIPT_NAME = "foo.py"


def test_parse_args_help(capsys):
    sys.argv = [SCRIPT_NAME, "--help"]
    with pytest.raises(SystemExit):
        __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("usage:")


def test_parse_args_list(capsys):
    sys.argv = [SCRIPT_NAME, "--list"]

    __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("List of supported event sources:")


def test_parse_args_filtered(capsys):
    sys.argv = [SCRIPT_NAME, "--filtered-list", "ses/"]

    __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("Filtered list of supported event sources:")


def test_generate_updated_schema_content():
    sys.argv = [SCRIPT_NAME, "-e", "ses/ses.json", "-f", "name", "-r", "us-east-1"]
    with mock.patch("aws_lambda_publish_shared_event.__main__.get_session") as mock_boto3:
        client = mock_boto3.return_value.client
        client.return_value.describe_schema.return_value = {"Content": '{"components": {"examples": {}}}'}

        __main__.main()

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
    assert __main__.get_test_event_path(str(expected)) == expected
