"""
MD2P3 CLI Tool
==============

This script converts Markdown files into PowerPoint (.pptx) presentations
using a predefined slide map. It supports configurable flags defined in
the toolFlags JSON configuration.
"""

import re
import string
import argparse
import pathlib
import json
import sys
from pptx import Presentation
from typing import Dict, Any, List, Tuple, Optional

from core.md2p3.slide import CoverSlide, NoticeSlide, AgendaSlide, ThemeSlide, ContentSlide, FinalSlide
from core.md2p3.help import printHelp

from lib.filesystem.accessible import readableFile, writableFile

# --- Load Configurations ---
try:
    toolSettingsAddress = (pathlib.Path(__file__).parent / "../conf/tools/md2p3.json").resolve()
    with toolSettingsAddress.open("r", encoding="utf-8") as file:
        toolSettings: Dict[str, Any] = json.load(file)

    flagsPath = pathlib.Path(__file__).parent / toolSettings["ToolFlagsFile"]
    with flagsPath.resolve().open("r", encoding="utf-8") as file:
        toolFlags: Dict[str, Any] = json.load(file)
except Exception as error:
    sys.exit(f"[Error] Failed to load configuration files: {error}")

# --- Default Files ---
defaultTemplateAddress: pathlib.Path = (pathlib.Path(__file__).parent / toolSettings["DefaultPPTX"]).resolve()
defaultSlideMapAddress: pathlib.Path = (pathlib.Path(__file__).parent / toolSettings["DefaultSlideMap"]).resolve()

# --- Helpers ---
def sanitiseFilename(name: str) -> str:
    """Replace invalid filename characters with safe ones."""
    validChars = f"-_.() {string.ascii_letters}{string.digits}"
    return "".join(c if c in validChars else "_" for c in name)

def processMarkdown(mdPath: pathlib.Path, templatePath: pathlib.Path, outputFolder: pathlib.Path,
                    slideMap: Dict[str, Any], prefix: str, tabSize: int) -> None:
    """Convert a Markdown file into a PowerPoint presentation."""
    if not readableFile(mdPath):
        print(f"[Error] Markdown file {mdPath} does not exist or is not readable.")
        return
    if not readableFile(templatePath):
        print(f"[Error] Template file {templatePath} does not exist or is not readable.")
        return

    try:
        presentation = Presentation(templatePath)
        with mdPath.open("r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as error:
        print(f"[Error] Failed to open template or Markdown file: {error}")
        return

    coverTitle: Optional[str] = None
    h1Blocks: List[str] = []
    contentBlocks: Dict[str, List[Tuple[str, str, List[Tuple[str, int]]]]] = {}
    currentH1 = currentH2 = currentH3 = None
    currentBullets: List[Tuple[str, int]] = []

    # --- Parse Markdown ---
    for line in lines:
        line = line.rstrip()
        if line.startswith("# "):
            if currentH2 and currentH3:
                contentBlocks.setdefault(currentH1, []).append((currentH2, currentH3, currentBullets))
                currentH3, currentBullets = None, []
            h1Text = line.strip("# ").strip()
            if h1Text.startswith(prefix):
                coverTitle = h1Text.replace(prefix, "", 1)
            else:
                h1Blocks.append(h1Text)
            currentH1, currentH2, currentH3 = h1Text, None, None
        elif line.startswith("## "):
            if currentH2 and currentH3:
                contentBlocks.setdefault(currentH1, []).append((currentH2, currentH3, currentBullets))
                currentH3, currentBullets = None, []
            currentH2 = line.strip("# ").strip()
        elif line.startswith("### "):
            if currentH2 and currentH3:
                contentBlocks.setdefault(currentH1, []).append((currentH2, currentH3, currentBullets))
                currentBullets = []
            currentH3 = line.strip("# ").strip()
        elif re.match(r"^(\s*)- ", line):
            indentString = re.match(r"^(\s*)- ", line).group(1)
            indentExpanded = indentString.replace("\t", " " * tabSize)
            level = len(indentExpanded) // tabSize
            currentBullets.append((line.strip("- ").strip(), level))

    if currentH2 and currentH3:
        contentBlocks.setdefault(currentH1, []).append((currentH2, currentH3, currentBullets))

    # --- Build Slides ---
    try:
        cover = CoverSlide(
            layoutIndex=slideMap["CoverSlide"]["LayoutIndex"],
            titlePlaceholder=slideMap["CoverSlide"]["TitlePlaceholder"],
            title=sanitiseFilename(coverTitle or toolSettings["DefaultPPTXTitle"]),
            slideIndex=slideMap["CoverSlide"]["SlideIndex"]
        )
        cover.integrateWith(presentation)

        notice = NoticeSlide(layoutIndex=slideMap["NoticeSlide"]["LayoutIndex"])
        notice.integrateWith(presentation)

        if h1Blocks:
            agenda = AgendaSlide(
                layoutIndex=slideMap["AgendaSlide"]["LayoutIndex"],
                tocPlaceholder=slideMap["AgendaSlide"]["ToCPlaceholder"],
                h1Blocks=h1Blocks
            )
            agenda.integrateWith(presentation)

        for h1 in h1Blocks:
            theme = ThemeSlide(
                layoutIndex=slideMap["ThemeSlide"]["LayoutIndex"],
                titlePlaceholder=slideMap["ThemeSlide"]["TitlePlaceholder"],
                title=h1
            )
            theme.integrateWith(presentation)

            if h1 in contentBlocks:
                for h2, h3, bullets in contentBlocks[h1]:
                    contentSlide = ContentSlide(
                        layoutIndex=slideMap["ContentSlide"]["LayoutIndex"],
                        h2Placeholder=slideMap["ContentSlide"]["H2Placeholder"],
                        h2Title=h2,
                        h3Placeholder=slideMap["ContentSlide"]["H3Placeholder"],
                        h3Title=h3,
                        contentPlaceholder=slideMap["ContentSlide"]["ListPlaceholder"],
                        content=bullets
                    )
                    contentSlide.integrateWith(presentation)

        final = FinalSlide(
            layoutIndex=slideMap["FinalSlide"]["LayoutIndex"],
            titlePlaceholder=slideMap["FinalSlide"]["TitlePlaceholder"],
            title=slideMap["FinalSlide"]["DefaultTitle"]
        )
        final.integrateWith(presentation)

        outputFilename = sanitiseFilename(coverTitle or toolSettings["DefaultOutputFileName"]) + ".pptx"
        outputPath = pathlib.Path(outputFolder) / outputFilename

        if not writableFile(outputPath):
            print(f"[Error] Cannot write to {outputPath}. Check permissions or path.")
            return

        presentation.save(outputPath)
        print(f"[Success] Presentation created: {outputPath}")

    except Exception as error:
        print(f"[Error] Failed to build presentation: {error}")

# --- CLI Entrypoint ---
if __name__ == "__main__":
    # --- Preemptive flag interception ---
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        if len(sys.argv) == 2:
            printHelp()
            sys.exit(0)
        for arg in sys.argv[1:]:
            if arg in ("-s", "--src"):
                printHelp("--src")
                sys.exit(0)
            elif arg in ("-d", "--destination"):
                printHelp("--destination")
                sys.exit(0)
            elif arg in ("-t", "--template"):
                printHelp("--template")
                sys.exit(0)
            elif arg in ("-m", "--slide-map"):
                printHelp("--slide-map")
                sys.exit(0)
            elif arg in ("-p", "--title-prefix"):
                printHelp("--title-prefix")
                sys.exit(0)
            elif arg in ("-x", "--tab"):
                printHelp("--tab")
                sys.exit(0)
            elif arg in ("-v", "--version"):
                printHelp("--version")
                sys.exit(0)
        printHelp()
        sys.exit(0)

    if any(arg in ("-v", "--version") for arg in sys.argv[1:]):
        print(f"MD2P3 Tool version {toolSettings.get('Version', 'Unknown')}")
        sys.exit(0)

    # --- Normal workflow only runs if help/version was not requested ---
    parser = argparse.ArgumentParser(description="Convert Markdown files to PPTX presentations.")
    parser.add_argument(toolFlags.get("Source", {}).get("shortcut", "-s"),
                        toolFlags.get("Source", {}).get("flag", "--src"),
                        dest="src", help="Input folder containing markdown files")
    parser.add_argument(toolFlags.get("Destination", {}).get("shortcut", "-d"),
                        toolFlags.get("Destination", {}).get("flag", "--destination"),
                        dest="destination", help="Output folder for PPTX files")
    parser.add_argument(toolFlags.get("Template", {}).get("shortcut", "-t"),
                        toolFlags.get("Template", {}).get("flag", "--template"),
                        dest="template", nargs="?", default=str(defaultTemplateAddress),
                        help="Custom PPTX template file to use")
    parser.add_argument(toolFlags.get("SlideMap", {}).get("shortcut", "-m"),
                        toolFlags.get("SlideMap", {}).get("flag", "--slide-map"),
                        dest="slideMapPath", nargs="?", default=str(defaultSlideMapAddress),
                        help="Custom Slide Map JSON file to use")
    parser.add_argument(toolFlags.get("TitlePrefix", {}).get("shortcut", "-p"),
                        toolFlags.get("TitlePrefix", {}).get("flag", "--title-prefix"),
                        dest="titlePrefix", nargs="?", default=str(toolSettings.get("DefaultPPTXTitlePrefix", "PPT: ")),
                        help="Prefix string used to identify the cover slide title heading in Markdown")
    parser.add_argument(toolFlags.get("TabSize", {}).get("shortcut", "-x"),
                        toolFlags.get("TabSize", {}).get("flag", "--tab"),
                        dest="tabSize", type=int, default=4,
                        help="Number of spaces to treat one tab as (default: 4)")

    args = parser.parse_args()

    # --- Validate required arguments ---
    if not args.src or not args.destination:
        parser.error("Both --src and --destination must be provided.")

    srcFolder: pathlib.Path = pathlib.Path(args.src).resolve()
    destinationFolder: pathlib.Path = pathlib.Path(args.destination).resolve()

    if not srcFolder.exists() or not srcFolder.is_dir():
        sys.exit(f"[Error] Source folder {srcFolder} does not exist or is not a directory.")

    destinationFolder.mkdir(parents=True, exist_ok=True)

    # --- Validate template and slide map ---
    templatePath: pathlib.Path = pathlib.Path(args.template).resolve()
    slideMapPath: pathlib.Path = pathlib.Path(args.slideMapPath).resolve()

    if not readableFile(templatePath):
        sys.exit(f"[Error] Template file {templatePath} does not exist or is not readable.")
    if not readableFile(slideMapPath):
        sys.exit(f"[Error] Slide map file {slideMapPath} does not exist or is not readable.")

    try:
        with slideMapPath.open("r", encoding="utf-8") as file:
            slideMap = json.load(file)
    except Exception as error:
        sys.exit(f"[Error] Failed to load slide map JSON: {error}")

    # --- Process Markdown files ---
    mdFiles = list(srcFolder.glob("*.md"))
    if not mdFiles:
        sys.exit(f"[Error] No Markdown files found in {srcFolder}.")

    for mdFile in mdFiles:
        processMarkdown(mdFile, templatePath, destinationFolder, slideMap, args.titlePrefix, args.tabSize)
