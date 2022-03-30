import argparse
import json
import sys
from typing import List

from aws_lambda_publish_shared_event.util import build_test_event, handle_list_arguments


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse arguments from the cli"""
    parser = argparse.ArgumentParser(prog="generate-test-event", description="Generated a local test event")
    parser.add_argument("-l", "--list", dest="list", help="List of supported event sources", action="store_true")
    parser.add_argument("--filtered-list", dest="filtered_list", help="Filtered list")
    parser.add_argument("event", help="Event source", nargs="?", default=None)
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    if handle_list_arguments(args):
        return True
    event = args.event
    if event is None:
        raise SystemExit("No event source specified")

    print(json.dumps(build_test_event(None, event)[1], indent=4))


if __name__ == "__main__":
    main()
