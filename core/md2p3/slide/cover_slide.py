"""
Cover Slide Class
=================

Represents the cover slide in a presentation. Extends the base Slide
class with a title placeholder object.

Functional Overview
-------------------
- Inherits from the abstract Slide base class.
- Accepts a placeholder object directly from JSON (with "Index" and "Name").
- Integrates into a PowerPoint presentation by:
  * Removing duplicate placeholders with the same idx.
  * Matching placeholders by both idx and name for reliability.
  * Clearing the title placeholder.
  * Applying Markdown-style formatting to the title text.
- Provides defensive checks for constructor arguments.
- Ensures graceful failure if integration encounters errors.

Contents
--------
class CoverSlide(Slide)
    Represents the cover slide in a presentation.
"""

from typing import Optional, Dict
from pptx import Presentation

from core.md2p3.slide import Slide
from lib.text.format_text import formatText


class CoverSlide(Slide):
    """
    CoverSlide extends Slide with a title placeholder object.

    Attributes
    ----------
    layoutIndex : int
        Index of the layout in the target template file.
    titlePlaceholder : Dict[str, object]
        JSON-derived dictionary containing placeholder metadata:
        {
            "Index": int,
            "Name": str
        }
    title : str
        Title text for the cover slide.
    slideIndex : Optional[int]
        Position of the slide in the output presentation, if specified.
    """

    def __init__(
        self,
        layoutIndex: int,
        titlePlaceholder: Dict[str, object],
        title: str,
        slideIndex: Optional[int] = None,
    ) -> None:
        """
        Initialise a CoverSlide object.

        Parameters
        ----------
        layoutIndex : int
            Index of the layout in the target template file.
        titlePlaceholder : Dict[str, object]
            JSON-derived dictionary containing placeholder metadata with keys:
            - "Index": int
            - "Name": str
        title : str
            Title text for the cover slide.
        slideIndex : Optional[int], default=None
            Position of the slide in the output presentation.

        Raises
        ------
        TypeError
            If placeholder object is invalid or title is not a string.
        """
        super().__init__(layoutIndex, slideIndex)

        if not isinstance(titlePlaceholder, dict):
            raise TypeError("titlePlaceholder must be a dictionary.")
        if not isinstance(titlePlaceholder.get("Index"), int):
            raise TypeError("titlePlaceholder['Index'] must be an integer.")
        if not isinstance(titlePlaceholder.get("Name"), str):
            raise TypeError("titlePlaceholder['Name'] must be a string.")
        if not isinstance(title, str):
            raise TypeError("title must be a string.")

        self._titlePlaceholder: Dict[str, object] = titlePlaceholder
        self._title: str = title

    @property
    def titlePlaceholder(self) -> Dict[str, object]:
        """Return the title placeholder metadata dictionary."""
        return self._titlePlaceholder

    @property
    def title(self) -> str:
        """Return the title text for the cover slide."""
        return self._title

    def integrateWith(self, presentation: Presentation) -> None:
        """
        Integrate the cover slide into the presentation.

        Parameters
        ----------
        presentation : pptx.Presentation
            The PowerPoint presentation object to integrate into.

        Notes
        -----
        - Uses the slideIndex to select the existing cover slide.
        - Removes all placeholders except the one matching both idx and name.
        - Clears the title placeholder and reuses its default paragraph.
        - Applies Markdown-style formatting to the title text.

        Raises
        ------
        RuntimeError
            If no matching placeholder is found or integration fails.
        """
        try:
            if self.slideIndex is None:
                raise ValueError("slideIndex must be set for CoverSlide integration.")

            slide = presentation.slides[self.slideIndex]

            # --- Identify and keep the correct placeholder ---
            targetPlaceholder = None
            for shape in list(slide.placeholders):
                if (
                    shape.placeholder_format.idx == self._titlePlaceholder["Index"]
                    and shape.name.strip() == self._titlePlaceholder["Name"]
                    and targetPlaceholder is None
                ):
                    targetPlaceholder = shape.text_frame
                else:
                    # Remove all other placeholders
                    sp = shape._element
                    sp.getparent().remove(sp)

            if targetPlaceholder is None:
                raise RuntimeError(
                    f"No matching placeholder found for idx={self._titlePlaceholder['Index']} "
                    f"and name='{self._titlePlaceholder['Name']}'."
                )

            # --- Populate title placeholder ---
            targetPlaceholder.clear()
            paragraph = targetPlaceholder.paragraphs[0]
            formatText(paragraph, self._title)

        except Exception as error:
            print(f"[Error] Failed to integrate CoverSlide: {error}")
            raise RuntimeError("Integration of CoverSlide failed.") from error
