import sys

import pytest

from src.aws_lambda_publish_shared_event.__main__ import main

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
