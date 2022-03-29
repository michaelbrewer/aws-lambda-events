import sys

import pytest

from aws_lambda_publish_shared_event.generate_test_event import __main__

SCRIPT_NAME = "foo.py"


def test_parse_args_no_args():
    # GIVEN no arguments
    sys.argv = []

    # WHEN calling `generate-test-event`
    with pytest.raises(SystemExit) as e:
        __main__.main()

    # THEN raise SystemExit
    assert str(e.value) == "No event source specified"


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


def test_generate_event(capsys):
    # GIVEN
    sys.argv = [SCRIPT_NAME, "ses/ses.json"]

    # WHEN
    __main__.main()

    # THEN
    captured = capsys.readouterr()
    assert captured.out.startswith("{\n")
