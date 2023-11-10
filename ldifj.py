#!/usr/bin/env python
# coding: utf-8

import argparse
import json
import sys
from io import BytesIO

from ldif import LDIFParser
from rich import print, print_json
from rich_argparse import RichHelpFormatter


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatter)
    parser.add_argument(
        "--metadata",
        "-m",
        help="Include metadata",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "FILE",
        nargs="?",
        help="LDIF file to parse, set to '-' to read from stdin",
        type=argparse.FileType("r"),
    )
    return parser, parser.parse_args()


def divide_ldif(content):
    sections = content.split("\n\n")
    metadata = sections[0]
    records = sections[1:]
    return metadata, records


class MyLDIF(LDIFParser):
    def __init__(self, input_file):
        LDIFParser.__init__(self, input_file)
        self.entries = []

    def handle(self, dn, entry):
        """Process a single LDIF entry"""
        processed_entry = {
            k: (
                vs[0].decode("utf-8", "replace")
                if isinstance(vs[0], bytes)
                else vs[0]
                if len(vs) == 1
                else [
                    v.decode("utf-8", "replace") if isinstance(v, bytes) else v
                    for v in vs
                ]
            )
            for k, vs in entry.items()
        }
        processed_entry["dn"] = dn

        self.entries.append(processed_entry)


def parse_ldif(record):
    record_bytes = BytesIO(record.encode("utf-8"))
    parser = MyLDIF(record_bytes)
    parser.parse()
    return parser.entries


def main():
    parser, args = parse_args()

    if not args.FILE or args.FILE == "-":
        if sys.stdin.isatty():
            parser.print_help()
            sys.exit(2)
        content = sys.stdin.read()
    else:
        content = args.FILE.read()

    metadata, records = divide_ldif(content)

    all_entries = []
    for record in records:
        try:
            entries = parse_ldif(record)
            all_entries.extend(entries)
        except ValueError as e:
            print(f"Skipping invalid record: {e}", file=sys.stderr)

    output = (
        {"metadata": metadata, "entries": all_entries}
        if args.metadata
        else all_entries
    )

    print_json(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
