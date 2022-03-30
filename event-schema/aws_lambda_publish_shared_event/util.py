import argparse
import json
import os
from fnmatch import fnmatch
from pathlib import Path
from typing import Dict, List, Optional, Tuple

template_root = f"{str(Path(__file__).parent)}/events/"


def list_of_test_events() -> List[str]:
    """Get the list of supported test events"""
    templates: List[str] = []
    for path, _, files in os.walk(template_root):
        templates.extend(
            removeprefix(template_root, os.path.join(path, name)) for name in files if fnmatch(name, "*.json")
        )
    templates.sort()
    return templates


def removeprefix(prefix: str, string: str) -> str:
    """Remove the prefix from the string"""
    return string[len(prefix) :] if string.startswith(prefix) else string


def get_test_event_path(event_path: str) -> Path:
    """Get the Path for the relative path events and then fall back to one of the standard test events"""
    if os.path.exists(event_path):
        return Path(event_path)
    else:
        return Path(template_root + event_path)


def build_test_event(event_name: Optional[str], event_path: str) -> Tuple[str, Dict]:
    """Load the event and return the event name and the parsed event"""
    path = get_test_event_path(event_path)
    event_name = event_name or path.name.replace(".json", "")
    event = json.loads(path.read_text())
    return event_name, event


def handle_list_arguments(args: argparse.Namespace) -> bool:
    """Handle any of the list arguments (-l, --filter-list) and return True if processed"""
    if args.list:
        print("List of supported event sources:")
        print(*list_of_test_events(), sep="\n")
        return True
    if args.filtered_list:
        filtered_list = list(filter(lambda x: x.startswith(args.filtered_list), list_of_test_events()))
        print("Filtered list of supported event sources:")
        print(*filtered_list, sep="\n")
        return True
    return False
