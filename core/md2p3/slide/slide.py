"""
Slide Base Class (Abstract)
===========================

This module defines the abstract base class for all slide builders in a
PowerPoint automation workflow. It provides a consistent foundation for
specialised slide types (e.g., title slides, content slides, thematic
slides, chart slides) by enforcing a common interface and shared
behaviour.

Functional Overview
-------------------
- Establishes common attributes for all slide types:
  * layoutIndex: index of the layout in the target template file.
  * slideIndex: optional position of the slide in the output presentation.
- Provides helper methods to:
  * Add a new slide from a given layout.
  * Restore design-time placeholder names to runtime slides.
- Enforces implementation of `integrateWith()` in subclasses.
- Ensures type safety and defensive checks for constructor arguments.
- Protects against runtime errors with structured exception handling.

Contents
--------
class Slide(ABC)
    Abstract base class for all slide types.
"""

from typing import Optional
from abc import ABC, abstractmethod

from pptx import Presentation
from pptx.slide import Slide as PptxSlide, SlideLayout

class Slide(ABC):
    """
    Abstract base class for all slide types.

    Attributes
    ----------
    layoutIndex : int
        Index of the layout in the target template file.
    slideIndex : Optional[int]
        Position of the slide in the output presentation, if specified.

    Notes
    -----
    - Subclasses must implement the `integrateWith()` method.
    - Provides helper methods to add slides and restore placeholder names.
    - Ensures consistency and reliability across all slide types.
    """

    def __init__(self, layoutIndex: int, slideIndex: Optional[int] = None) -> None:
        """
        Initialise a Slide object with layout and optional slide index.

        Parameters
        ----------
        layoutIndex : int
            Index of the layout in the target template file.
        slideIndex : Optional[int], default=None
            Position of the slide in the output presentation.

        Raises
        ------
        TypeError
            If layoutIndex is not an integer or slideIndex is not an integer when provided.
        """
        if not isinstance(layoutIndex, int):
            raise TypeError("layoutIndex must be an integer.")
        if slideIndex is not None and not isinstance(slideIndex, int):
            raise TypeError("slideIndex must be an integer if provided.")

        self._layoutIndex: int = layoutIndex
        self._slideIndex: Optional[int] = slideIndex

    @property
    def layoutIndex(self) -> int:
        """
        Return the layout index of the slide.

        Returns
        -------
        int
            The layout index.
        """
        return self._layoutIndex

    @property
    def slideIndex(self) -> Optional[int]:
        """
        Return the slide index if available.

        Returns
        -------
        Optional[int]
            The slide index, or None if not specified.
        """
        return self._slideIndex

    def keepLayoutNames(self, slide: PptxSlide, slideLayout: SlideLayout) -> None:
        """
        Restore placeholder names in a slide to match those in the given slide layout.

        This method handles both unique and duplicate indices by aligning
        placeholders in order when necessary.

        Parameters
        ----------
        slide : pptx.slide.Slide
            The instantiated slide whose placeholder names will be updated.
        slideLayout : pptx.slide.SlideLayout
            The layout used to create the slide, providing design-time names.
        """
        try:
            # Build a mapping of idx -> list of layout placeholders
            layoutMap = {}
            for layoutPlaceholder in slideLayout.placeholders:
                layoutMap.setdefault(layoutPlaceholder.placeholder_format.idx, []).append(layoutPlaceholder)

            # Track how many times each idx has been seen
            seenCounts = {}

            for slidePlaceholder in slide.placeholders:
                idx = slidePlaceholder.placeholder_format.idx
                count = seenCounts.get(idx, 0)

                if idx in layoutMap and count < len(layoutMap[idx]):
                    slidePlaceholder.name = layoutMap[idx][count].name
                    seenCounts[idx] = count + 1
        except Exception as error:
            print(f"[Error] Failed to restore layout names: {error}")

    def addSlide(self, presentation: Presentation) -> PptxSlide:
        """
        Add a new slide using this slide's layout index and restore placeholder names.

        Parameters
        ----------
        presentation : pptx.Presentation
            The PowerPoint presentation object.

        Returns
        -------
        pptx.slide.Slide
            The newly added slide with placeholder names restored.

        Raises
        ------
        RuntimeError
            If the slide cannot be added or names cannot be restored.
        """
        try:
            slideLayout = presentation.slide_layouts[self.layoutIndex]
            slide = presentation.slides.add_slide(slideLayout)
            self.keepLayoutNames(slide, slideLayout)
            return slide
        except Exception as error:
            print(f"[Error] Failed to add slide: {error}")
            raise RuntimeError("Slide creation failed.") from error

    @abstractmethod
    def integrateWith(self, presentation: Presentation) -> None:
        """
        Abstract method to integrate this slide into the given Presentation.

        Parameters
        ----------
        presentation : pptx.Presentation
            The PowerPoint presentation object to integrate into.

        Notes
        -----
        - Subclasses must implement this method to define how the slide
          is added to the presentation and populated with content.
        - Typical implementations may add a new slide based on the
          specified layoutIndex and populate it with text, images, or charts.
        """
        raise NotImplementedError("Subclasses must implement integrateWith().")
