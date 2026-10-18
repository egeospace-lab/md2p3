"""
print_layout_info.py
====================

This module provides functionality for displaying layout and placeholder
metadata extracted from PowerPoint (.pptx) template files. It defines the
`printLayoutInfo` function, which formats and prints the metadata in a
human-readable form to the console.

Functional Overview
-------------------
- Accepts layout metadata previously extracted from a PPTX template.
- Prints each slide layout with its index and name.
- For each layout, lists all placeholders with their index and name.
- Provides clear console output to help users visually inspect the
  structure of slide layouts.
- Useful for developers validating template structures, designers checking
  placeholder consistency, and content creators preparing automated workflows.

Contents
--------
printLayoutInfo(layoutsInfo: List[Dict[str, Any]], templatePath: pathlib.Path) -> None
    Print layout and placeholder metadata to stdout in a structured format.
"""

import pathlib
from typing import Dict, Any, List


def printLayoutInfo(layoutsInfo: List[Dict[str, Any]], templatePath: pathlib.Path) -> None:
    """
    Print layout and placeholder metadata to stdout.

    This function formats and displays the extracted layout information
    in a human-readable form. Each layout is listed with its index and name,
    followed by its placeholders (index and name). The output is structured
    to make inspection of slide layouts straightforward.

    Parameters
    ----------
    layoutsInfo : List[Dict[str, Any]]
        Extracted layout metadata from the template. Each dictionary should
        contain 'LayoutIndex', 'LayoutName', and a list of 'Placeholders'.
    templatePath : pathlib.Path
        Path to the PowerPoint template file being analysed.

    Examples
    --------
    Print layouts from a template in the current directory:
        >>> printLayoutInfo(layoutsInfo, pathlib.Path("myTemplate.pptx"))

    Print layouts from an absolute path:
        >>> printLayoutInfo(layoutsInfo, pathlib.Path("/home/user/templates/myTemplate.pptx"))
    """
    try:
        print(f"\n======== Layouts and Placeholders in {templatePath.name} ========")

        if not layoutsInfo:
            print("[Info] No layouts found or extraction failed.")
        else:
            for layout in layoutsInfo:
                layoutIndex = layout.get("LayoutIndex")
                layoutName = layout.get("LayoutName")
                print(f"\nLayout {layoutIndex}: {layoutName}")

                placeholders = layout.get("Placeholders", [])
                if placeholders:
                    for placeholder in placeholders:
                        idx = placeholder.get("Index")
                        name = placeholder.get("Name")
                        print(f"  - Placeholder idx={idx}, name={name}")
                else:
                    print("  [No placeholders detected]")

        print("\n====== End of Layouts and Placeholders ======\n")

    except Exception as error:
        print(f"[Error] Failed to print layout information: {error}")
