"""
print_help.py
=============

Provides the `printHelp` function to display CLI documentation for the
PPTX Layout Viewer. Supports both general and flag-specific help.

Functional Overview
-------------------
- Without arguments, prints full tool documentation (usage, options, examples).
- With a specific flag, prints documentation for that flag only.
- Designed to intercept execution when `--help` (`-h`) or `--version` (`-v`) is passed.

Contents
--------
printHelp(flag: Optional[str] = None) -> None
    Display CLI help information for the PPTX Layout Viewer.
"""

from typing import Optional


def printHelp(flag: Optional[str] = None) -> None:
    """
    Display CLI help information for the PPTX Layout Viewer.

    Parameters
    ----------
    flag : Optional[str], default=None
        Specific flag to show help for. If None, prints general documentation.

    Raises
    ------
    TypeError
        If flag is not a string.
    ValueError
        If flag is not recognised.
    """

    # Expanded general tool documentation
    toolDoc = """
PPTX Layout Viewer
==================

A command-line utility to inspect PowerPoint (.pptx) templates by extracting
and displaying slide layout and placeholder metadata. This tool is useful for:

- Developers automating presentation workflows.
- Designers validating template consistency.
- Content creators ensuring placeholders are correctly defined.

Usage
-----
python3 -m bin.view_layout [options]

Options
-------
-h, --help
    Show help information. If used alone, prints the full tool documentation.
    If combined with another flag, prints documentation for that flag only.

-v, --version
    Show the current version of the PPTX Layout Viewer.

-t, --template <path>
    Path to the PPTX template file to analyse. Defaults to the configured
    template if not provided. Supports both relative and absolute paths.

-e, --export
    Export layout information to JSON instead of printing to stdout.
    Useful for integrating with other tools or pipelines. Requires -d or
    --destination flag.

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
"""

    # Expanded flag-specific documentation with examples
    flagDocs = {
        "-h": """Help Flag
---------
Displays help information. If used alone, prints the full tool documentation.
If combined with another flag, prints documentation for that flag only.

Examples
--------
Show all help:
    python3 -m bin.view_layout -h

Show help for template flag:
    python3 -m bin.view_layout -h -t""",
        "--help": """Help Flag
---------
Displays help information. If used alone, prints the full tool documentation.
If combined with another flag, prints documentation for that flag only.

Examples
--------
Show all help:
    python3 -m bin.view_layout --help

Show help for export flag:
    python3 -m bin.view_layout --help --export""",
        "-v": """Version Flag
--------------
Displays the current version of the PPTX Layout Viewer.

Examples
--------
Show version:
    python3 -m bin.view_layout -v""",
        "--version": """Version Flag
--------------
Displays the current version of the PPTX Layout Viewer.

Examples
--------
Show version:
    python3 -m bin.view_layout --version""",
        "-t": """Template Flag
-------------
Specify the PPTX template file to analyse. Supports relative and absolute paths.

Examples
--------
Analyse a template in the current directory:
    python3 -m bin.view_layout -t myTemplate.pptx

Analyse a template using an absolute path:
    python3 -m bin.view_layout -t /home/user/templates/myTemplate.pptx""",
        "--template": """Template Flag
-------------
Specify the PPTX template file to analyse. Supports relative and absolute paths.

Examples
--------
Analyse a template in the current directory:
    python3 -m bin.view_layout --template myTemplate.pptx

Analyse a template using an absolute path:
    python3 -m bin.view_layout --template /home/user/templates/myTemplate.pptx""",
        "-e": """Export Flag
-----------
Enable export mode. Layout information will be written to JSON instead of printed.

Examples
--------
Export layouts to stdout:
    python3 -m bin.view_layout -t myTemplate.pptx

Export layouts to a file (requires -d):
    python3 -m bin.view_layout -t myTemplate.pptx -e -d layouts.json""",
        "--export": """Export Flag
-----------
Enable export mode. Layout information will be written to JSON instead of printed.

Examples
--------
Export layouts to stdout:
    python3 -m bin.view_layout --template myTemplate.pptx

Export layouts to a file (requires --destination):
    python3 -m bin.view_layout --template myTemplate.pptx --export --destination layouts.json""",
        "-d": """Destination Flag
----------------
Specify the destination JSON file path for export. Required if export mode is enabled.

Examples
--------
Export layouts to a file:
    python3 -m bin.view_layout -t myTemplate.pptx -e -d output/layouts.json""",
        "--destination": """Destination Flag
----------------
Specify the destination JSON file path for export. Required if export mode is enabled.

Examples
--------
Export layouts to a file:
    python3 -m bin.view_layout --template myTemplate.pptx --export --destination output/layouts.json""",
    }

    # Defensive programming: ensure flag is either None or a string
    if flag is not None and not isinstance(flag, str):
        raise TypeError("Flag must be a string or None.")

    try:
        if flag:
            if flag in flagDocs:
                print(f"\n{flagDocs[flag]}\n")
            else:
                raise ValueError(f"Unrecognised flag: {flag}")
        else:
            print(toolDoc)
    except Exception as error:
        print(f"[Error] Failed to display help information: {error}")
