import sys

import pytest

from aws_lambda_publish_shared_event.generate_test_event import __main__

SCRIPT_NAME = "foo.py"


def test_parse_no_args():
    sys.argv = []
    with pytest.raises(SystemExit) as e:
        __main__.main()

    assert str(e.value) == "No event source specified"


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


def test_generate_event(capsys):
    sys.argv = [SCRIPT_NAME, "ses/ses.json"]

    __main__.main()

    captured = capsys.readouterr()
    assert captured.out.startswith("{\n")
