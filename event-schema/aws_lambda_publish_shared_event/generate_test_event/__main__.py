import argparse
import json
import sys
from typing import List

from aws_lambda_publish_shared_event.util import build_test_event, list_of_test_events


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse arguments from the cli"""
    parser = argparse.ArgumentParser(
        prog="generate-test-event", description="Generated a local test event to the system out"
    )
    parser.add_argument("-l", "--list", dest="list", help="List of supported event sources", action="store_true")
    parser.add_argument("event", help="Event source", nargs="?", default=None)
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    if args.list:
        print("List of supported event sources:")
        print(*list_of_test_events(), sep="\n")
        return

    event = args.event
    if event is None:
        raise SystemExit("No event source specified")

    print(json.dumps(build_test_event(None, event)[1], indent=4))


if __name__ == "__main__":
    main()
