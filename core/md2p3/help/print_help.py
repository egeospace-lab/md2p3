"""
print_help.py
=============

Provides the `printHelp` function to display CLI documentation for the
MD2P3 (Markdown to PowerPoint) Tool. Supports both general and flag-specific help.

Functional Overview
-------------------
- Without arguments, prints full tool documentation (usage, options, examples).
- With a specific flag, prints documentation for that flag only.
- Designed to intercept execution when `--help` (`-h`) or `--version` (`-v`) is passed.

Contents
--------
printHelp(flag: Optional[str] = None) -> None
    Display CLI help information for the MD2P3 Tool.
"""

from typing import Optional


def printHelp(flag: Optional[str] = None) -> None:
    """
    Display CLI help information for the MD2P3 Tool.

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
MD2P3 Tool
==========

A command-line utility to convert Markdown (.md) files into PowerPoint (.pptx)
presentations using a predefined slide map. This tool is useful for:

- Developers automating presentation generation.
- Content creators preparing structured slides from Markdown notes.
- Teams standardising presentation templates.

Usage
-----
python3 -m bin.md2p3 [options]

Options
-------
-h, --help
    Show help information. If used alone, prints the full tool documentation.
    If combined with another flag, prints documentation for that flag only.

-v, --version
    Show the current version of the MD2P3 Tool.

-s, --src <path>
    Source folder containing Markdown files to convert.

-d, --destination <path>
    Destination folder where generated PPTX files will be saved.

-t, --template <path>
    Path to the PPTX template file to use. Defaults to the configured template.

-m, --slide-map <path>
    Path to the Slide Map JSON file. Defaults to the configured slide map.

-p, --title-prefix <string>
    Prefix string used to identify the special heading in the Markdown file
    that becomes the **cover slide title**. Only one such heading is expected.
    All other top-level headings (`# Heading`) are treated as **theme slides**.

-x, --tab <int>
    Number of spaces to treat one tab as (default: 4).

Examples
--------
Convert Markdown files in a folder:
    python3 -m bin.md2p3 -s ./notes -d ./output

Use a custom template and slide map:
    python3 -m bin.md2p3 -s ./notes -d ./output -t custom.pptx -m custom_map.json

Specify a cover slide prefix:
    python3 -m bin.md2p3 -s ./notes -d ./output -p "Cover: "

Show tool version:
    python3 -m bin.md2p3 -v
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
    python3 -m bin.md2p3 -h

Show help for source flag:
    python3 -m bin.md2p3 -h -s""",
        "--help": """Help Flag
---------
Displays help information. If used alone, prints the full tool documentation.
If combined with another flag, prints documentation for that flag only.

Examples
--------
Show all help:
    python3 -m bin.md2p3 --help

Show help for destination flag:
    python3 -m bin.md2p3 --help --destination""",
        "-v": """Version Flag
--------------
Displays the current version of the MD2P3 Tool.

Examples
--------
Show version:
    python3 -m bin.md2p3 -v""",
        "--version": """Version Flag
--------------
Displays the current version of the MD2P3 Tool.

Examples
--------
Show version:
    python3 -m bin.md2p3 --version""",
        "-s": """Source Flag
-------------
Specify the folder containing Markdown files to convert.

Examples
--------
Convert Markdown files in a folder:
    python3 -m bin.md2p3 -s ./notes -d ./output""",
        "--src": """Source Flag
-------------
Specify the folder containing Markdown files to convert.

Examples
--------
Convert Markdown files in a folder:
    python3 -m bin.md2p3 --src ./notes --destination ./output""",
        "-d": """Destination Flag
----------------
Specify the folder where generated PPTX files will be saved.

Examples
--------
Save presentations to a folder:
    python3 -m bin.md2p3 -s ./notes -d ./output""",
        "--destination": """Destination Flag
----------------
Specify the folder where generated PPTX files will be saved.

Examples
--------
Save presentations to a folder:
    python3 -m bin.md2p3 --src ./notes --destination ./output""",
        "-t": """Template Flag
-------------
Specify a custom PPTX template file to use.

Examples
--------
Use a custom template:
    python3 -m bin.md2p3 -s ./notes -d ./output -t custom.pptx""",
        "--template": """Template Flag
-------------
Specify a custom PPTX template file to use.

Examples
--------
Use a custom template:
    python3 -m bin.md2p3 --src ./notes --destination ./output --template custom.pptx""",
        "-m": """Slide Map Flag
----------------
Specify a custom Slide Map JSON file to use.

Examples
--------
Use a custom slide map:
    python3 -m bin.md2p3 -s ./notes -d ./output -m custom_map.json""",
        "--slide-map": """Slide Map Flag
----------------
Specify a custom Slide Map JSON file to use.

Examples
--------
Use a custom slide map:
    python3 -m bin.md2p3 --src ./notes --destination ./output --slide-map custom_map.json""",
        "-p": """Title Prefix Flag
------------------
Specify the prefix string used to identify the special heading in the Markdown
file that becomes the **cover slide title**. Only one such heading is expected.
All other top-level headings are treated as **theme slides**.

Examples
--------
Use a custom title prefix:
    python3 -m bin.md2p3 -s ./notes -d ./output -p "Cover: """,
        "--title-prefix": """Title Prefix Flag
------------------
Specify the prefix string used to identify the special heading in the Markdown
file that becomes the **cover slide title**. Only one such heading is expected.
All other top-level headings are treated as **theme slides**.

Examples
--------
Use a custom title prefix:
    python3 -m bin.md2p3 --src ./notes --destination ./output --title-prefix "Cover: """,
        "-x": """Tab Size Flag
--------------
Specify the number of spaces to treat one tab as (default: 4).

Examples
--------
Use a custom tab size:
    python3 -m bin.md2p3 -s ./notes -d ./output -x 2""",
        "--tab": """Tab Size Flag
--------------
Specify the number of spaces to treat one tab as (default: 4).

Examples
--------
Use a custom tab size:
    python3 -m bin.md2p3 --src ./notes --destination ./output --tab 2""",
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
