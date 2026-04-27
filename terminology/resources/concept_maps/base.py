"""Base classes for data-driven FHIR ConceptMap resources.

This module provides:

- ``MappingEntry`` — a typed DTO representing a single source→target concept
  mapping row, including display names, relationship, and an optional comment.

- ``MappedConceptMap`` — a ``ConceptMap`` subclass whose groups are built
  automatically from a ``MAPPINGS`` class variable (a list of
  ``MappingEntry``).  Subclasses only need to declare ``MAPPINGS``,
  implement ``static_url()``, and pass the result of ``_build_groups()`` to
  ``super().__init__()``.  Reverse ConceptMaps become trivial: inherit the
  same ``MAPPINGS`` and call ``_build_groups(direction="reverse")``.
"""

from dataclasses import dataclass, field
from typing import ClassVar, Dict, List, Tuple

from terminology.fhir_types import ConceptMap


_REVERSE_RELATIONSHIP: Dict[str, str] = {
    "wider": "narrower",
    "narrower": "wider",
}


@dataclass
class MappingEntry:
    """DTO for a single concept mapping row.

    Fields
    ------
    src_system:
        Canonical URL of the source CodeSystem.
    src_code:
        Code in the source CodeSystem.
    tgt_system:
        Canonical URL of the target CodeSystem.
    tgt_code:
        Code in the target CodeSystem.
    relationship:
        FHIR ConceptMap relationship value.  Defaults to ``"equivalent"``.
        Supported values: ``"equivalent"``, ``"wider"``, ``"narrower"``,
        ``"inexact"``, ``"not-related-to"``.
    src_display:
        Human-readable display for the source code (optional).
    tgt_display:
        Human-readable display for the target code (optional).
    comment:
        Free-text comment on the mapping (optional).
    """

    src_system: str
    src_code: str
    tgt_system: str
    tgt_code: str
    relationship: str = "equivalent"
    src_display: str = ""
    tgt_display: str = ""
    comment: str = ""


class MappedConceptMap(ConceptMap):
    """ConceptMap base class driven by a ``MAPPINGS`` class variable.

    Subclasses declare two class variables:

    ``MAPPINGS``
        A list of :class:`MappingEntry` objects describing every source→target
        concept pair.

    ``EXTRA_GROUP_PAIRS``
        An optional list of ``(source_url, target_url)`` tuples for groups that
        should appear in the output even when no mapping entries reference them
        (e.g. to declare intent for systems not yet mapped).

    Subclasses must also implement :meth:`static_url` and call
    ``_build_groups()`` (or ``_build_groups(direction="reverse")``) when
    constructing the ``group`` argument passed to ``super().__init__()``.
    """

    MAPPINGS: ClassVar[List[MappingEntry]] = []
    EXTRA_GROUP_PAIRS: ClassVar[List[Tuple[str, str]]] = []

    @classmethod
    def static_url(cls) -> str:
        raise NotImplementedError(f"{cls.__name__} must implement static_url()")

    @classmethod
    def _build_groups(cls, direction: str = "forward") -> List[Dict]:
        """Build FHIR ConceptMap ``group`` dicts from ``MAPPINGS``.

        Parameters
        ----------
        direction:
            ``"forward"`` (default) produces source→target groups.
            ``"reverse"`` swaps source and target, and inverts asymmetric
            relationships (``wider`` ↔ ``narrower``).

        Returns
        -------
        List[Dict]
            Ready to pass as the ``group`` field of a FHIR ConceptMap.
        """
        groups: Dict[str, Dict] = {}

        for entry in cls.MAPPINGS:
            if direction == "forward":
                group_key = entry.tgt_system
                group_source = entry.src_system
                group_target = entry.tgt_system
                element_code = entry.src_code
                element_display = entry.src_display
                target_code = entry.tgt_code
                target_display = entry.tgt_display
                relationship = entry.relationship
            else:
                group_key = entry.src_system
                group_source = entry.tgt_system
                group_target = entry.src_system
                element_code = entry.tgt_code
                element_display = entry.tgt_display
                target_code = entry.src_code
                target_display = entry.src_display
                relationship = _REVERSE_RELATIONSHIP.get(entry.relationship, entry.relationship)

            if group_key not in groups:
                groups[group_key] = {
                    "source": group_source,
                    "target": group_target,
                    "element": [],
                }

            tgt_entry: Dict = {"code": target_code, "relationship": relationship}
            if target_display:
                tgt_entry["display"] = target_display
            if entry.comment:
                tgt_entry["comment"] = entry.comment

            element: Dict = {"code": element_code}
            if element_display:
                element["display"] = element_display
            element["target"] = [tgt_entry]

            groups[group_key]["element"].append(element)

        # Ensure declared groups exist even with no mappings
        for src_url, tgt_url in cls.EXTRA_GROUP_PAIRS:
            if direction == "forward":
                key = tgt_url
                src, tgt = src_url, tgt_url
            else:
                key = src_url
                src, tgt = tgt_url, src_url
            if key not in groups:
                groups[key] = {"source": src, "target": tgt, "element": []}

        return list(groups.values())


__all__ = ["MappingEntry", "MappedConceptMap"]
