"""
export_layout_info.py
=====================

This module provides functionality for exporting layout and placeholder
metadata extracted from PowerPoint (.pptx) template files. It defines the
`exportLayoutInfo` function, which writes the metadata to a JSON file at
a specified destination path.

Functional Overview
-------------------
- Accepts layout metadata previously extracted from a PPTX template.
- Ensures the destination directory exists, creating it if necessary.
- Validates that the destination file path is writable before exporting.
- Writes the metadata to a JSON file in a structured, indented format.
- Handles common errors gracefully, including permission issues and
  unexpected exceptions, while providing clear console feedback.

Contents
--------
exportLayoutInfo(layoutsInfo: List[Dict[str, Any]], destinationPath: pathlib.Path) -> None
    Export layout and placeholder metadata to a JSON file. Prints success
    or error messages to the console depending on the outcome.
"""

import pathlib
import json
from typing import Dict, Any, List

from lib.filesystem.accessible import writableFile


def exportLayoutInfo(layoutsInfo: List[Dict[str, Any]], destinationPath: pathlib.Path) -> None:
    """
    Export layout and placeholder metadata to a JSON file.

    This function writes the extracted layout information to a JSON file
    at the specified destination path. It ensures that the destination
    directory exists, validates writability, and handles permission errors
    gracefully.

    Parameters
    ----------
    layoutsInfo : List[Dict[str, Any]]
        Extracted layout metadata from the template. Each dictionary
        typically contains slide layout names, placeholder details,
        and associated attributes.
    destinationPath : pathlib.Path
        Path to the output JSON file where the metadata will be saved.
        Can be relative or absolute. Parent directories are created
        automatically if they do not exist.

    Raises
    ------
    TypeError
        If destinationPath is not a pathlib.Path instance.
    PermissionError
        If the process lacks permission to write to the destination.
    Exception
        For unexpected errors during export.

    Examples
    --------
    Export layouts to a file in the current directory:
        >>> exportLayoutInfo(layoutsInfo, pathlib.Path("layouts.json"))

    Export layouts to a nested directory (auto-created):
        >>> exportLayoutInfo(layoutsInfo, pathlib.Path("output/data/layouts.json"))
    """
    try:
        if not isinstance(destinationPath, pathlib.Path):
            raise TypeError("destinationPath must be a pathlib.Path instance.")

        # Ensure parent directory exists
        destinationPath.parent.mkdir(parents=True, exist_ok=True)

        # Validate writability before attempting export
        if not writableFile(destinationPath):
            raise PermissionError(f"Destination path {destinationPath} is not writable.")

        # Write metadata to JSON file with indentation for readability
        with destinationPath.open("w", encoding="utf-8") as file:
            json.dump(layoutsInfo, file, indent=4)

        print(f"[Success] Layout information exported successfully to {destinationPath}")

    except PermissionError as error:
        print(f"[Error] No write permission for {destinationPath}. "
              f"Try running with appropriate permissions or choose another path. Details: {error}")
    except Exception as error:
        print(f"[Error] Failed to export layout information: {error}")
