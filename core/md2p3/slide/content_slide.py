"""
Content Slide Class
===================

Represents a content slide in a presentation. Extends the base Slide
class with H2 title, H3 title, and a list of content bullet points.

Functional Overview
-------------------
- Inherits from the abstract Slide base class.
- Accepts placeholder objects directly from JSON (with "Index" and "Name").
- Adds attributes for H2 title, H3 title, and content bullets.
- Integrates into a PowerPoint presentation by:
  * Removing duplicate placeholders with the same idx.
  * Matching placeholders by both idx and name for reliability.
  * Clearing placeholders for H2, H3, and content.
  * Applying Markdown-style formatting to titles and bullet points.
  * Respecting bullet nesting levels.
- Provides defensive checks for constructor arguments.
- Ensures graceful failure if integration encounters errors.

Contents
--------
class ContentSlide(Slide)
    Represents a content slide in a presentation.
"""

from typing import Optional, List, Tuple, Dict
from pptx import Presentation

from core.md2p3.slide import Slide
from lib.text.format_text import formatText


class ContentSlide(Slide):
    """
    ContentSlide extends Slide with H2 title, H3 title, and content bullets.

    Attributes
    ----------
    layoutIndex : int
        Index of the layout in the target template file.
    h2Placeholder : Dict[str, object]
        JSON-derived dictionary containing placeholder metadata for H2 title:
        {
            "Index": int,
            "Name": str
        }
    h2Title : str
        The H2 title text for the content slide.
    h3Placeholder : Dict[str, object]
        JSON-derived dictionary containing placeholder metadata for H3 title:
        {
            "Index": int,
            "Name": str
        }
    h3Title : str
        The H3 title text for the content slide.
    contentPlaceholder : Dict[str, object]
        JSON-derived dictionary containing placeholder metadata for content bullets:
        {
            "Index": int,
            "Name": str
        }
    content : List[Tuple[str, int]]
        List of bullet point tuples (text, level).
    slideIndex : Optional[int]
        Position of the slide in the output presentation, if specified.
    """

    def __init__(
        self,
        layoutIndex: int,
        h2Placeholder: Dict[str, object],
        h2Title: str,
        h3Placeholder: Dict[str, object],
        h3Title: str,
        contentPlaceholder: Dict[str, object],
        content: List[Tuple[str, int]],
        slideIndex: Optional[int] = None,
    ) -> None:
        """
        Initialise a ContentSlide object.

        Parameters
        ----------
        layoutIndex : int
            Index of the layout in the target template file.
        h2Placeholder : Dict[str, object]
            JSON-derived dictionary containing placeholder metadata for H2 title.
        h2Title : str
            The H2 title text for the content slide.
        h3Placeholder : Dict[str, object]
            JSON-derived dictionary containing placeholder metadata for H3 title.
        h3Title : str
            The H3 title text for the content slide.
        contentPlaceholder : Dict[str, object]
            JSON-derived dictionary containing placeholder metadata for content bullets.
        content : List[Tuple[str, int]]
            List of bullet point tuples (text, level).
        slideIndex : Optional[int], default=None
            Position of the slide in the output presentation.

        Raises
        ------
        TypeError
            If placeholder objects are invalid, titles are not strings,
            or content is not a list of (text, level) tuples.
        """
        super().__init__(layoutIndex, slideIndex)

        # Validate placeholders
        for placeholder, name in [
            (h2Placeholder, "h2Placeholder"),
            (h3Placeholder, "h3Placeholder"),
            (contentPlaceholder, "contentPlaceholder"),
        ]:
            if not isinstance(placeholder, dict):
                raise TypeError(f"{name} must be a dictionary.")
            if not isinstance(placeholder.get("Index"), int):
                raise TypeError(f"{name}['Index'] must be an integer.")
            if not isinstance(placeholder.get("Name"), str):
                raise TypeError(f"{name}['Name'] must be a string.")

        # Validate titles
        if not all(isinstance(val, str) for val in (h2Title, h3Title)):
            raise TypeError("h2Title and h3Title must be strings.")

        # Validate content
        if not isinstance(content, list) or not all(
            isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str) and isinstance(item[1], int)
            for item in content
        ):
            raise TypeError("content must be a list of (text, level) tuples.")

        self._h2Placeholder: Dict[str, object] = h2Placeholder
        self._h2Title: str = h2Title

        self._h3Placeholder: Dict[str, object] = h3Placeholder
        self._h3Title: str = h3Title

        self._contentPlaceholder: Dict[str, object] = contentPlaceholder
        self._content: List[Tuple[str, int]] = content

    def integrateWith(self, presentation: Presentation) -> None:
        """
        Integrate the content slide into the presentation.

        Parameters
        ----------
        presentation : pptx.Presentation
            The PowerPoint presentation object to integrate into.

        Notes
        -----
        - Adds a new slide using the specified layout.
        - Removes all placeholders except those matching both idx and name for H2, H3, and content.
        - Clears each placeholder before inserting text.
        - Applies Markdown-style formatting to H2, H3, and bullet points.
        - Bullet points respect nesting levels.

        Raises
        ------
        RuntimeError
            If any required placeholder is not found or integration fails.
        """
        try:
            # --- Add new slide using the specified layout ---
            slide = self.addSlide(presentation)

            # --- Identify and keep the correct placeholders ---
            h2PlaceholderFrame = h3PlaceholderFrame = contentPlaceholderFrame = None
            for shape in list(slide.placeholders):
                if (
                    shape.placeholder_format.idx == self._h2Placeholder["Index"]
                    and shape.name.strip() == self._h2Placeholder["Name"]
                    and h2PlaceholderFrame is None
                ):
                    h2PlaceholderFrame = shape.text_frame
                elif (
                    shape.placeholder_format.idx == self._h3Placeholder["Index"]
                    and shape.name.strip() == self._h3Placeholder["Name"]
                    and h3PlaceholderFrame is None
                ):
                    h3PlaceholderFrame = shape.text_frame
                elif (
                    shape.placeholder_format.idx == self._contentPlaceholder["Index"]
                    and shape.name.strip() == self._contentPlaceholder["Name"]
                    and contentPlaceholderFrame is None
                ):
                    contentPlaceholderFrame = shape.text_frame
                else:
                    sp = shape._element
                    sp.getparent().remove(sp)

            if not all([h2PlaceholderFrame, h3PlaceholderFrame, contentPlaceholderFrame]):
                raise RuntimeError("One or more required placeholders not found for ContentSlide.")

            # --- Populate H2 ---
            h2PlaceholderFrame.clear()
            formatText(h2PlaceholderFrame.add_paragraph(), self._h2Title)

            # --- Populate H3 ---
            h3PlaceholderFrame.clear()
            formatText(h3PlaceholderFrame.add_paragraph(), self._h3Title)

            # --- Populate bullets with nesting ---
            contentPlaceholderFrame.clear()
            for text, level in self._content:
                paragraph = contentPlaceholderFrame.add_paragraph()
                formatText(paragraph, text, bulletLevel=level)

        except Exception as error:
            print(f"[Error] Failed to integrate ContentSlide: {error}")
            raise RuntimeError("Integration of ContentSlide failed.") from error
