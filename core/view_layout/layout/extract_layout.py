"""
extract_layout.py
=================

This module provides functionality for extracting layout and placeholder
metadata from PowerPoint (.pptx) template files. It defines the
`extractLayout` function, which opens a given template and iterates through
all available slide layouts to collect structural information.

Functional Overview
-------------------
- Opens a specified PPTX template file using the `python-pptx` library.
- Iterates through each slide layout in the template.
- For each layout, gathers metadata including:
  * Layout index
  * Layout name
  * Placeholder details (index and name)
- Returns the collected information as a list of dictionaries, suitable for
  printing to stdout or exporting to JSON.
- Ensures graceful failure if the file cannot be opened or parsed.

Contents
--------
extractLayout(templatePath: pathlib.Path) -> List[Dict[str, Any]]
    Extract layout and placeholder metadata from a PowerPoint template.
    Returns an empty list if the file cannot be opened or parsed.
"""

import pathlib
from typing import Dict, Any, List
from pptx import Presentation


def extractLayout(templatePath: pathlib.Path) -> List[Dict[str, Any]]:
    """
    Extract layout and placeholder metadata from a PowerPoint template.

    This function opens the specified PPTX file and iterates through all
    available slide layouts. For each layout, it collects metadata such as
    the layout index, layout name, and placeholder details (index and name).

    Parameters
    ----------
    templatePath : pathlib.Path
        Path to the PowerPoint template file to be analysed. Supports both
        relative and absolute paths.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries, each representing a slide layout and its
        associated placeholders. Returns an empty list if the file cannot
        be opened or parsed.

    Raises
    ------
    TypeError
        If templatePath is not a pathlib.Path instance.

    Examples
    --------
    Extract layouts from a template in the current directory:
        >>> extractLayout(pathlib.Path("myTemplate.pptx"))

    Extract layouts from an absolute path:
        >>> extractLayout(pathlib.Path("/home/user/templates/myTemplate.pptx"))
    """
    try:
        if not isinstance(templatePath, pathlib.Path):
            raise TypeError("templatePath must be a pathlib.Path instance.")

        # Load the presentation
        presentation: Presentation = Presentation(templatePath)

    except Exception as error:
        print(f"[Error] Failed to open PPTX file: {error}")
        return []

    layoutsInfo: List[Dict[str, Any]] = []

    try:
        # Iterate through each slide layout and collect metadata
        for layoutIndex, layout in enumerate(presentation.slide_layouts):
            placeholdersInfo = [
                {
                    "Index": placeholder.placeholder_format.idx,
                    "Name": placeholder.name,
                }
                for placeholder in layout.placeholders
            ]

            layoutsInfo.append(
                {
                    "LayoutIndex": layoutIndex,
                    "LayoutName": layout.name,
                    "Placeholders": placeholdersInfo,
                }
            )
    except Exception as error:
        print(f"[Error] Failed to extract layout metadata: {error}")
        return []

    return layoutsInfo
