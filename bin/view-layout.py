"""
view_layout.py
==============

PPTX Layout Viewer
------------------

This command-line utility inspects PowerPoint (.pptx) templates by extracting
and displaying slide layout and placeholder metadata. It is designed for
developers, designers, and content creators who need to understand the
structure of slide layouts before building automated presentation workflows.

Functional Overview
-------------------
- Loads a predefined template file specified in configuration, or a custom
  template path via the `--template` (`-t`) flag.
- Extracts layout and placeholder metadata using the `python-pptx` library.
- Prints metadata to stdout in a structured format, or exports it to JSON
  using the `--export` (`-e`) flag with a destination path via `--destination` (`-d`).
- Provides a dedicated help system (`--help` / `-h`) and version system
  (`--version` / `-v`) that intercept execution to display documentation
  or version information before exiting.

Flags
-----
-h, --help
    Show help information. If used alone, prints the full tool documentation.
    If combined with another flag, prints documentation for that flag only.

-v, --version
    Show the current version of the PPTX Layout Viewer.

-t, --template <path>
    Path to the PPTX template file to analyse. Defaults to the configured
    template if not provided. Supports relative and absolute paths.

-e, --export
    Export layout information to JSON instead of printing to stdout.

-d, --destination <path>
    Destination JSON file path for export. Required if --export/-e is used.
    Ensure the directory exists and is writable.

Examples
--------
View layouts from a template:
    python3 -m bin.view_layout -t myTemplate.pptx

Export layouts to JSON:
    python3 -m bin.view_layout -t myTemplate.pptx -e -d layouts.json

Show tool version:
    python3 -m bin.view_layout -v

Chain with other tools (e.g., jq for filtering):
    python3 -m bin.view_layout -t myTemplate.pptx -e | jq '.layouts[0]'
"""

import sys
import argparse
import pathlib
import json
from typing import Dict, Any, List

from core.view_layout.help import printHelp
from core.view_layout.layout import extractLayout, printLayoutInfo, exportLayoutInfo
from md2p3.lib.filesystem.accessible import readableFile

# --- Load Configurations ---
try:
    configPath = pathlib.Path(__file__).parent / "../conf/tools/view-layout.json"
    with configPath.resolve().open("r", encoding="utf-8") as file:
        toolSettings: Dict[str, Any] = json.load(file)

    flagsPath = pathlib.Path(__file__).parent / toolSettings["ToolFlagsFile"]
    with flagsPath.resolve().open("r", encoding="utf-8") as file:
        toolFlags: Dict[str, Any] = json.load(file)

except Exception as error:
    sys.exit(f"[Error] Failed to load configuration files: {error}")


def main() -> None:
    """
    CLI entrypoint for the PPTX Layout Viewer.

    Workflow
    --------
    1. Intercept `--help`/`-h` first. If present, print the appropriate help
       message and exit immediately.
    2. Intercept `--version`/`-v`. If present, print the tool version and exit.
    3. Parse remaining arguments using argparse.
    4. Validate the input template file for existence and readability.
    5. Extract layout and placeholder metadata from the template.
    6. Depending on flags:
       - Print metadata to stdout, OR
       - Export metadata to a JSON file at the specified destination.
    """
    # --- Preemptive --help interception (highest priority) ---
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        if len(sys.argv) == 2:
            printHelp()
            sys.exit(0)
        for arg in sys.argv[1:]:
            if arg in ("-t", "--template"):
                printHelp("--template")
                sys.exit(0)
            elif arg in ("-e", "--export"):
                printHelp("--export")
                sys.exit(0)
            elif arg in ("-d", "--destination"):
                printHelp("--destination")
                sys.exit(0)
            elif arg in ("-v", "--version"):
                printHelp("--version")
                sys.exit(0)
        printHelp()
        sys.exit(0)

    # --- Preemptive --version interception (second priority) ---
    if any(arg in ("-v", "--version") for arg in sys.argv[1:]):
        print(f"PPTX Layout Viewer version {toolSettings.get('Version', 'Unknown')}")
        sys.exit(0)

    # --- Normal workflow only runs if help/version was not requested ---
    parser: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        toolFlags.get("Template", {}).get("shortcut", "-t"),
        toolFlags.get("Template", {}).get("flag", "--template"),
        dest="template",
        nargs="?",
        default=str((pathlib.Path(__file__).parent / toolSettings["DefaultPPTX"]).resolve()),
        help="PPTX file whose layout information has to be extracted"
    )
    parser.add_argument(
        toolFlags.get("Export", {}).get("shortcut", "-e"),
        toolFlags.get("Export", {}).get("flag", "--export"),
        dest="export",
        action="store_true",
        help="Export layout information to JSON"
    )
    parser.add_argument(
        toolFlags.get("Destination", {}).get("shortcut", "-d"),
        toolFlags.get("Destination", {}).get("flag", "--destination"),
        dest="destination",
        help="Destination JSON file path for export (required if --export/-e is used)"
    )

    args: argparse.Namespace = parser.parse_args()
    templatePath: pathlib.Path = pathlib.Path(args.template).resolve()

    # --- Validate template file ---
    if not readableFile(templatePath):
        sys.exit(f"[Error] PPTX file at {templatePath} does not exist or is inaccessible.")

    # --- Extract layout metadata ---
    layoutsInfo: List[Dict[str, Any]] = extractLayout(templatePath)
    if not layoutsInfo:
        sys.exit("[Error] No layout information could be extracted.")

    # --- Output based on flags ---
    if args.export:
        if not args.destination:
            sys.exit("[Error] --destination/-d must be provided when using --export/-e")
        exportLayoutInfo(layoutsInfo, pathlib.Path(args.destination).resolve())
    else:
        printLayoutInfo(layoutsInfo, templatePath)


if __name__ == "__main__":
    main()
