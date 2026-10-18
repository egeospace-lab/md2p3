"""
accessible.py
=============

This module provides utility functions for checking file accessibility.
It defines functions that validate whether a given path points to a file
that is readable, writable, or executable by the current process.

Functional Overview
-------------------
- Accepts a `pathlib.Path` object representing a file path.
- Verifies that the path exists and refers to a file (not a directory).
- Provides checks for:
  * Readability (`readableFile`)
  * Writability (`writableFile`)
  * Executability (`executableFile`)
- Returns `True` if all checks pass, otherwise `False`.
- Handles unexpected errors gracefully by returning `False`.

Contents
--------
readableFile(filePath: pathlib.Path) -> bool
    Validate that a given path points to a readable file.

writableFile(filePath: pathlib.Path) -> bool
    Validate that a given path points to a writable file.

executableFile(filePath: pathlib.Path) -> bool
    Validate that a given path points to an executable file.
"""

import os
import pathlib

def readableFile(filePath: pathlib.Path) -> bool:
    """
    Validate that a given path points to a readable file.

    Parameters
    ----------
    filePath : pathlib.Path
        Path to the file to validate.

    Returns
    -------
    bool
        True if the path exists, is a file, and is readable.
        False otherwise.
    """
    try:
        return filePath.exists() and filePath.is_file() and os.access(filePath, os.R_OK)
    except Exception as error:
        print(f"[Warning] readableFile failed: {error}")
        return False

def writableFile(filePath: pathlib.Path) -> bool:
    """
    Validate that a given path points to a writable file, or can be created.

    Parameters
    ----------
    filePath : pathlib.Path
        Path to the file to validate.

    Returns
    -------
    bool
        True if the path exists and is writable, or if the parent directory
        can be created and the file can be written. False otherwise.
    """
    try:
        # Ensure parent directory exists (create if necessary)
        parentDir = filePath.parent
        if not parentDir.exists():
            parentDir.mkdir(parents=True, exist_ok=True)

        # If file already exists, check writability
        if filePath.exists():
            return filePath.is_file() and os.access(filePath, os.W_OK)

        # If file does not exist, check if we can create it
        try:
            with open(filePath, "w", encoding="utf-8") as testFile:
                testFile.write("")  # create empty file
            filePath.unlink(missing_ok=True)  # remove test file
            return True
        except Exception:
            return False

    except Exception as error:
        print(f"[Warning] writableFile failed: {error}")
        return False

def executableFile(filePath: pathlib.Path) -> bool:
    """
    Validate that a given path points to an executable file.

    Parameters
    ----------
    filePath : pathlib.Path
        Path to the file to validate.

    Returns
    -------
    bool
        True if the path exists, is a file, and is executable.
        False otherwise.
    """
    try:
        return filePath.exists() and filePath.is_file() and os.access(filePath, os.X_OK)
    except Exception as error:
        print(f"[Warning] executableFile failed: {error}")
        return False
