"""
Agenda Slide Class
==================

Represents the agenda slide in a presentation. Extends the base Slide
class with a ToC placeholder object and a list of H1 blocks.

Functional Overview
-------------------
- Inherits from the abstract Slide base class.
- Accepts a placeholder object directly from JSON (with "Index" and "Name").
- Integrates into a PowerPoint presentation by:
  * Removing duplicate placeholders with the same idx.
  * Matching placeholders by both idx and name for reliability.
  * Clearing the ToC placeholder.
  * Adding each H1 block as a bullet point at level 0.
- Provides methods to extend the agenda dynamically.
- Ensures type-safety and graceful failure handling.

Contents
--------
class AgendaSlide(Slide)
    Represents the agenda slide in a presentation.
"""

from typing import Optional, List, Union, Dict
from pptx import Presentation

from core.md2p3.slide import Slide
from lib.text.format_text import formatText


class AgendaSlide(Slide):
    """
    AgendaSlide extends Slide with a ToC placeholder object and H1 blocks.

    Attributes
    ----------
    layoutIndex : int
        Index of the layout in the target template file.
    tocPlaceholder : Dict[str, object]
        JSON-derived dictionary containing placeholder metadata:
        {
            "Index": int,
            "Name": str
        }
    h1Blocks : List[str]
        List of H1 titles to populate the agenda slide.
    slideIndex : Optional[int]
        Position of the slide in the output presentation, if specified.
    """

    def __init__(
        self,
        layoutIndex: int,
        tocPlaceholder: Dict[str, object],
        h1Blocks: Optional[List[str]] = None,
        slideIndex: Optional[int] = None,
    ) -> None:
        """
        Initialise an AgendaSlide object.

        Parameters
        ----------
        layoutIndex : int
            Index of the layout in the target template file.
        tocPlaceholder : Dict[str, object]
            JSON-derived dictionary containing placeholder metadata with keys:
            - "Index": int
            - "Name": str
        h1Blocks : Optional[List[str]], default=None
            List of H1 titles to populate the agenda slide.
        slideIndex : Optional[int], default=None
            Position of the slide in the output presentation.

        Raises
        ------
        TypeError
            If placeholder object is invalid or h1Blocks contains non-string elements.
        """
        super().__init__(layoutIndex, slideIndex)

        if not isinstance(tocPlaceholder, dict):
            raise TypeError("tocPlaceholder must be a dictionary.")
        if not isinstance(tocPlaceholder.get("Index"), int):
            raise TypeError("tocPlaceholder['Index'] must be an integer.")
        if not isinstance(tocPlaceholder.get("Name"), str):
            raise TypeError("tocPlaceholder['Name'] must be a string.")
        if h1Blocks is not None and not all(isinstance(item, str) for item in h1Blocks):
            raise TypeError("h1Blocks must be a list of strings if provided.")

        self._tocPlaceholder: Dict[str, object] = tocPlaceholder
        self._h1Blocks: List[str] = h1Blocks or []

    @property
    def tocPlaceholder(self) -> Dict[str, object]:
        """Return the ToC placeholder metadata dictionary."""
        return self._tocPlaceholder

    @property
    def h1Blocks(self) -> List[str]:
        """Return a copy of the H1 blocks list."""
        return list(self._h1Blocks)

    def extendToC(self, newBlocks: Union[str, List[str]]) -> None:
        """
        Extend the table of contents with new H1 blocks.

        Parameters
        ----------
        newBlocks : Union[str, List[str]]
            A single string or a list of strings to add to the agenda.

        Notes
        -----
        - Strings are appended directly.
        - Lists are extended if all elements are strings.
        - Invalid input types are ignored with a warning.
        """
        if isinstance(newBlocks, str):
            self._h1Blocks.append(newBlocks)
        elif isinstance(newBlocks, list) and all(isinstance(item, str) for item in newBlocks):
            self._h1Blocks.extend(newBlocks)
        else:
            print("[Warning] extendToC expects a string or list of strings. Update ignored.")

    def integrateWith(self, presentation: Presentation) -> None:
        """
        Integrate the agenda slide into the presentation.

        Parameters
        ----------
        presentation : pptx.Presentation
            The PowerPoint presentation object to integrate into.

        Notes
        -----
        - Adds a new slide using the specified layout.
        - Removes all placeholders except the one matching both idx and name.
        - Clears the ToC placeholder before inserting content.
        - Adds each H1 block as a bullet point at level 0.

        Raises
        ------
        RuntimeError
            If no matching placeholder is found or integration fails.
        """
        try:
            # --- Add new slide using the specified layout ---
            slide = self.addSlide(presentation)

            # --- Identify and keep the correct placeholder ---
            targetPlaceholder = None
            for shape in list(slide.placeholders):
                if (
                    shape.placeholder_format.idx == self._tocPlaceholder["Index"]
                    and shape.name.strip() == self._tocPlaceholder["Name"]
                    and targetPlaceholder is None
                ):
                    targetPlaceholder = shape.text_frame
                else:
                    sp = shape._element
                    sp.getparent().remove(sp)

            if targetPlaceholder is None:
                raise RuntimeError(
                    f"No matching placeholder found for idx={self._tocPlaceholder['Index']} "
                    f"and name='{self._tocPlaceholder['Name']}'."
                )

            # --- Populate ToC placeholder ---
            targetPlaceholder.clear()
            for title in self._h1Blocks:
                paragraph = targetPlaceholder.add_paragraph()
                formatText(paragraph, title, bulletLevel=0)

        except Exception as error:
            print(f"[Error] Failed to integrate AgendaSlide: {error}")
            raise RuntimeError("Integration of AgendaSlide failed.") from error
