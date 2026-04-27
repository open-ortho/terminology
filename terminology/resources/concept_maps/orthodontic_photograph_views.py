"""ConceptMaps linking Open Ortho photographic views to SNOMED CT concepts.

Each class inherits :class:`~terminology.resources.concept_maps.base.MappedConceptMap`
and shares the same ``MAPPINGS`` list.  The forward map goes Open Ortho → SNOMED CT;
the reverse map goes SNOMED CT → Open Ortho.  Both are built automatically by
``_build_groups()``.

``EXTRA_GROUP_PAIRS`` ensures that the extraoral-3D and intraoral-3D code systems
appear as declared groups in the output even though no mappings exist for them yet,
signalling intent for future work.
"""

from datetime import datetime

from terminology.resources.concept_maps.base import MappedConceptMap, MappingEntry
from terminology.resources.naming_systems import OpenOrthoNamingSystem
from terminology.resources.code_systems.ada_1100_extraoral_2d_photographic_scheduled_protocol import (
    Extraoral2DPhotographicScheduledProtocolCodeSystem,
)
from terminology.resources.code_systems.ada_1100_extraoral_3d_visible_light_scheduled_protocol import (
    Extraoral3DVisibleLightScheduledProtocolCodeSystem,
)
from terminology.resources.code_systems.ada_1100_intraoral_2d_photographic_scheduled_protocol import (
    Intraoral2DPhotographicScheduledProtocolCodeSystem,
)
from terminology.resources.code_systems.ada_1100_intraoral_3d_visible_light_scheduled_protocol import (
    Intraoral3DVisibleLightScheduledProtocolCodeSystem,
)


SNOMED_SYSTEM_URL = "http://snomed.info/sct"

_EXTRAORAL_2D = Extraoral2DPhotographicScheduledProtocolCodeSystem.static_url()
_EXTRAORAL_3D = Extraoral3DVisibleLightScheduledProtocolCodeSystem.static_url()
_INTRAORAL_2D = Intraoral2DPhotographicScheduledProtocolCodeSystem.static_url()
_INTRAORAL_3D = Intraoral3DVisibleLightScheduledProtocolCodeSystem.static_url()

_E = MappingEntry  # local alias for brevity


class OrthodonticPhotographViewsConceptMap(MappedConceptMap):
    """Map Open Ortho photographic codes to SNOMED CT photographic concepts.

    Source systems are the ADA-1100 extraoral and intraoral 2D scheduled-protocol
    code systems.  The target system is SNOMED CT.  All relationships are
    ``equivalent``.

    ``EXTRA_GROUP_PAIRS`` declares the 3D visible-light code systems as
    participating groups even though no concept-level mappings exist yet.
    """

    MAPPINGS = [
        _E(_EXTRAORAL_2D, "EV01", SNOMED_SYSTEM_URL, "1306623000"),
        _E(_EXTRAORAL_2D, "EV02", SNOMED_SYSTEM_URL, "1306622005"),
        _E(_EXTRAORAL_2D, "EV03", SNOMED_SYSTEM_URL, "1306621003"),
        _E(_EXTRAORAL_2D, "EV04", SNOMED_SYSTEM_URL, "1306620002"),
        _E(_EXTRAORAL_2D, "EV05", SNOMED_SYSTEM_URL, "1306628009"),
        _E(_EXTRAORAL_2D, "EV06", SNOMED_SYSTEM_URL, "1306626008"),
        _E(_EXTRAORAL_2D, "EV07", SNOMED_SYSTEM_URL, "1365795009"),
        _E(_EXTRAORAL_2D, "EV08", SNOMED_SYSTEM_URL, "1306627004"),
        _E(_EXTRAORAL_2D, "EV09", SNOMED_SYSTEM_URL, "1306625007"),
        _E(_EXTRAORAL_2D, "EV10", SNOMED_SYSTEM_URL, "1306629001"),
        _E(_EXTRAORAL_2D, "EV11", SNOMED_SYSTEM_URL, "1306631005"),
        _E(_EXTRAORAL_2D, "EV12", SNOMED_SYSTEM_URL, "1306632003"),
        _E(_EXTRAORAL_2D, "EV13", SNOMED_SYSTEM_URL, "1306633008"),
        _E(_EXTRAORAL_2D, "EV14", SNOMED_SYSTEM_URL, "1306634002"),
        _E(_EXTRAORAL_2D, "EV15", SNOMED_SYSTEM_URL, "1306630006"),
        _E(_EXTRAORAL_2D, "EV16", SNOMED_SYSTEM_URL, "1306663004"),
        _E(_EXTRAORAL_2D, "EV17", SNOMED_SYSTEM_URL, "1306624006"),
        _E(_EXTRAORAL_2D, "EV18", SNOMED_SYSTEM_URL, "1306662009"),
        _E(_EXTRAORAL_2D, "EV19", SNOMED_SYSTEM_URL, "1306664005"),
        _E(_EXTRAORAL_2D, "EV20", SNOMED_SYSTEM_URL, "1306665006"),
        _E(_EXTRAORAL_2D, "EV21", SNOMED_SYSTEM_URL, "787611004"),
        _E(_EXTRAORAL_2D, "EV22", SNOMED_SYSTEM_URL, "1306656004"),
        _E(_EXTRAORAL_2D, "EV23", SNOMED_SYSTEM_URL, "1306648002"),
        _E(_EXTRAORAL_2D, "EV24", SNOMED_SYSTEM_URL, "1306649005"),
        _E(_EXTRAORAL_2D, "EV25", SNOMED_SYSTEM_URL, "1306650005"),
        _E(_EXTRAORAL_2D, "EV26", SNOMED_SYSTEM_URL, "1306651009"),
        _E(_EXTRAORAL_2D, "EV27", SNOMED_SYSTEM_URL, "1306652002"),
        _E(_EXTRAORAL_2D, "EV28", SNOMED_SYSTEM_URL, "1365794008"),
        _E(_EXTRAORAL_2D, "EV29", SNOMED_SYSTEM_URL, "1306644000"),
        _E(_EXTRAORAL_2D, "EV30", SNOMED_SYSTEM_URL, "1306645004"),
        _E(_EXTRAORAL_2D, "EV31", SNOMED_SYSTEM_URL, "1306646003"),
        _E(_EXTRAORAL_2D, "EV32", SNOMED_SYSTEM_URL, "1306647007"),
        _E(_EXTRAORAL_2D, "EV33", SNOMED_SYSTEM_URL, "1306643006"),
        _E(_EXTRAORAL_2D, "EV34", SNOMED_SYSTEM_URL, "1306654001"),
        _E(_EXTRAORAL_2D, "EV35", SNOMED_SYSTEM_URL, "1306655000"),
        _E(_EXTRAORAL_2D, "EV36", SNOMED_SYSTEM_URL, "1306653007"),
        _E(_EXTRAORAL_2D, "EV37", SNOMED_SYSTEM_URL, "1365796005"),
        _E(_EXTRAORAL_2D, "EV38", SNOMED_SYSTEM_URL, "1365797001"),
        _E(_EXTRAORAL_2D, "EV39", SNOMED_SYSTEM_URL, "1365798006"),
        _E(_EXTRAORAL_2D, "EV40", SNOMED_SYSTEM_URL, "1365790004"),
        _E(_EXTRAORAL_2D, "EV41", SNOMED_SYSTEM_URL, "1365791000"),
        _E(_EXTRAORAL_2D, "EV42", SNOMED_SYSTEM_URL, "1365793002"),
        _E(_EXTRAORAL_2D, "EV43", SNOMED_SYSTEM_URL, "1365792007"),
        _E(_INTRAORAL_2D, "IV01", SNOMED_SYSTEM_URL, "1365808006"),
        _E(_INTRAORAL_2D, "IV02", SNOMED_SYSTEM_URL, "1365814004"),
        _E(_INTRAORAL_2D, "IV03", SNOMED_SYSTEM_URL, "1365817006"),
        _E(_INTRAORAL_2D, "IV04", SNOMED_SYSTEM_URL, "1365800004"),
        _E(_INTRAORAL_2D, "IV05", SNOMED_SYSTEM_URL, "1365869001"),
        _E(_INTRAORAL_2D, "IV06", SNOMED_SYSTEM_URL, "1365870000"),
        _E(_INTRAORAL_2D, "IV07", SNOMED_SYSTEM_URL, "1365802007"),
        _E(_INTRAORAL_2D, "IV08", SNOMED_SYSTEM_URL, "1365801000"),
        _E(_INTRAORAL_2D, "IV09", SNOMED_SYSTEM_URL, "1365804008"),
        _E(_INTRAORAL_2D, "IV10", SNOMED_SYSTEM_URL, "1365803002"),
        _E(_INTRAORAL_2D, "IV11", SNOMED_SYSTEM_URL, "1365806005"),
        _E(_INTRAORAL_2D, "IV12", SNOMED_SYSTEM_URL, "1365807001"),
        _E(_INTRAORAL_2D, "IV13", SNOMED_SYSTEM_URL, "1365805009"),
        _E(_INTRAORAL_2D, "IV14", SNOMED_SYSTEM_URL, "1365824007"),
        _E(_INTRAORAL_2D, "IV15", SNOMED_SYSTEM_URL, "1365827000"),
        _E(_INTRAORAL_2D, "IV16", SNOMED_SYSTEM_URL, "1365826009"),
        _E(_INTRAORAL_2D, "IV17", SNOMED_SYSTEM_URL, "1365828005"),
        _E(_INTRAORAL_2D, "IV18", SNOMED_SYSTEM_URL, "1365809003"),
        _E(_INTRAORAL_2D, "IV19", SNOMED_SYSTEM_URL, "1365815003"),
        _E(_INTRAORAL_2D, "IV20", SNOMED_SYSTEM_URL, "1365818001"),
        _E(_INTRAORAL_2D, "IV21", SNOMED_SYSTEM_URL, "1365799003"),
        _E(_INTRAORAL_2D, "IV22", SNOMED_SYSTEM_URL, "1365868009"),
        _E(_INTRAORAL_2D, "IV23", SNOMED_SYSTEM_URL, "1365871001"),
        _E(_INTRAORAL_2D, "IV24", SNOMED_SYSTEM_URL, "1365863000"),
        _E(_INTRAORAL_2D, "IV25", SNOMED_SYSTEM_URL, "1365865007"),
        _E(_INTRAORAL_2D, "IV26", SNOMED_SYSTEM_URL, "1365864006"),
        _E(_INTRAORAL_2D, "IV27", SNOMED_SYSTEM_URL, "1365866008"),
        _E(_INTRAORAL_2D, "IV28", SNOMED_SYSTEM_URL, "1365867004"),
        _E(_INTRAORAL_2D, "IV29", SNOMED_SYSTEM_URL, "1365811007"),
        _E(_INTRAORAL_2D, "IV30", SNOMED_SYSTEM_URL, "1365810008"),
    ]

    EXTRA_GROUP_PAIRS = [
        (_EXTRAORAL_3D, SNOMED_SYSTEM_URL),
        (_INTRAORAL_3D, SNOMED_SYSTEM_URL),
    ]

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/ConceptMap/orthodontic-photograph-views"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name="OrthodonticPhotographViewsConceptMap",
            title="Orthodontic Photograph Views ConceptMap",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="OpenOrtho",
            description=(
                "Mapping between Open Ortho photographic views and SNOMED CT "
                "photographic concepts."
            ),
            sourceScopeUri=OpenOrthoNamingSystem().url,
            targetScopeUri=SNOMED_SYSTEM_URL,
            group=self._build_groups(direction="forward"),
        )


class OrthodonticPhotographViewsReverseConceptMap(MappedConceptMap):
    """Map SNOMED CT photographic concepts back to Open Ortho photographic codes.

    Shares ``MAPPINGS`` and ``EXTRA_GROUP_PAIRS`` with
    :class:`OrthodonticPhotographViewsConceptMap`; groups are built with
    ``direction="reverse"`` so source and target are swapped.
    """

    MAPPINGS = OrthodonticPhotographViewsConceptMap.MAPPINGS
    EXTRA_GROUP_PAIRS = OrthodonticPhotographViewsConceptMap.EXTRA_GROUP_PAIRS

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/ConceptMap/orthodontic-photograph-views-reverse"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name="OrthodonticPhotographViewsReverseConceptMap",
            title="Orthodontic Photograph Views Reverse ConceptMap",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="OpenOrtho",
            description=(
                "Reverse mapping between SNOMED CT photographic concepts and "
                "Open Ortho photographic views."
            ),
            sourceScopeUri=SNOMED_SYSTEM_URL,
            targetScopeUri=OpenOrthoNamingSystem().url,
            group=self._build_groups(direction="reverse"),
        )
