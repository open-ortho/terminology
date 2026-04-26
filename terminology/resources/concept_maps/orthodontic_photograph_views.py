"""ConceptMaps linking Open Ortho photographic views to SNOMED CT concepts."""

from datetime import datetime
from typing import Dict, Iterable, List, TypedDict, cast

from terminology.fhir_types import ConceptMap

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

SYSTEM_URLS = {
    "extraoral_2d": Extraoral2DPhotographicScheduledProtocolCodeSystem().url,
    "extraoral_3d": Extraoral3DVisibleLightScheduledProtocolCodeSystem().url,
    "intraoral_2d": Intraoral2DPhotographicScheduledProtocolCodeSystem().url,
    "intraoral_3d": Intraoral3DVisibleLightScheduledProtocolCodeSystem().url,
}

# Mappings for Open Ortho -> SNOMED CT (direction can be reversed on demand)
# Each entry: (oo_system_key, oo_code, snomed_code)
PHOTO_VIEW_MAPPINGS = [
    ("extraoral_2d", "EV01", "1306623000"),
    ("extraoral_2d", "EV02", "1306622005"),
    ("extraoral_2d", "EV03", "1306621003"),
    ("extraoral_2d", "EV04", "1306620002"),
    ("extraoral_2d", "EV05", "1306628009"),
    ("extraoral_2d", "EV06", "1306626008"),
    ("extraoral_2d", "EV07", "1365795009"),
    ("extraoral_2d", "EV08", "1306627004"),
    ("extraoral_2d", "EV09", "1306625007"),
    ("extraoral_2d", "EV10", "1306629001"),
    ("extraoral_2d", "EV11", "1306631005"),
    ("extraoral_2d", "EV12", "1306632003"),
    ("extraoral_2d", "EV13", "1306633008"),
    ("extraoral_2d", "EV14", "1306634002"),
    ("extraoral_2d", "EV15", "1306630006"),
    ("extraoral_2d", "EV16", "1306663004"),
    ("extraoral_2d", "EV17", "1306624006"),
    ("extraoral_2d", "EV18", "1306662009"),
    ("extraoral_2d", "EV19", "1306664005"),
    ("extraoral_2d", "EV20", "1306665006"),
    ("extraoral_2d", "EV21", "787611004"),
    ("extraoral_2d", "EV22", "1306656004"),
    ("extraoral_2d", "EV23", "1306648002"),
    ("extraoral_2d", "EV24", "1306649005"),
    ("extraoral_2d", "EV25", "1306650005"),
    ("extraoral_2d", "EV26", "1306651009"),
    ("extraoral_2d", "EV27", "1306652002"),
    ("extraoral_2d", "EV28", "1365794008"),
    ("extraoral_2d", "EV29", "1306644000"),
    ("extraoral_2d", "EV30", "1306645004"),
    ("extraoral_2d", "EV31", "1306646003"),
    ("extraoral_2d", "EV32", "1306647007"),
    ("extraoral_2d", "EV33", "1306643006"),
    ("extraoral_2d", "EV34", "1306654001"),
    ("extraoral_2d", "EV35", "1306655000"),
    ("extraoral_2d", "EV36", "1306653007"),
    ("extraoral_2d", "EV37", "1365796005"),
    ("extraoral_2d", "EV38", "1365797001"),
    ("extraoral_2d", "EV39", "1365798006"),
    ("extraoral_2d", "EV40", "1365790004"),
    ("extraoral_2d", "EV41", "1365791000"),
    ("extraoral_2d", "EV42", "1365793002"),
    ("extraoral_2d", "EV43", "1365792007"),
    ("intraoral_2d", "IV01", "1365808006"),
    ("intraoral_2d", "IV02", "1365814004"),
    ("intraoral_2d", "IV03", "1365817006"),
    ("intraoral_2d", "IV04", "1365800004"),
    ("intraoral_2d", "IV05", "1365869001"),
    ("intraoral_2d", "IV06", "1365870000"),
    ("intraoral_2d", "IV07", "1365802007"),
    ("intraoral_2d", "IV08", "1365801000"),
    ("intraoral_2d", "IV09", "1365804008"),
    ("intraoral_2d", "IV10", "1365803002"),
    ("intraoral_2d", "IV11", "1365806005"),
    ("intraoral_2d", "IV12", "1365807001"),
    ("intraoral_2d", "IV13", "1365805009"),
    ("intraoral_2d", "IV14", "1365824007"),
    ("intraoral_2d", "IV15", "1365827000"),
    ("intraoral_2d", "IV16", "1365826009"),
    ("intraoral_2d", "IV17", "1365828005"),
    ("intraoral_2d", "IV18", "1365809003"),
    ("intraoral_2d", "IV19", "1365815003"),
    ("intraoral_2d", "IV20", "1365818001"),
    ("intraoral_2d", "IV21", "1365799003"),
    ("intraoral_2d", "IV22", "1365868009"),
    ("intraoral_2d", "IV23", "1365871001"),
    ("intraoral_2d", "IV24", "1365863000"),
    ("intraoral_2d", "IV25", "1365865007"),
    ("intraoral_2d", "IV26", "1365864006"),
    ("intraoral_2d", "IV27", "1365866008"),
    ("intraoral_2d", "IV28", "1365867004"),
    ("intraoral_2d", "IV29", "1365811007"),
    ("intraoral_2d", "IV30", "1365810008"),
]


class ConceptMapGroup(TypedDict):
    source: str
    target: str
    element: List[Dict[str, object]]


def _build_groups(
    mappings: Iterable[tuple[str, str, str]],
    *,
    direction: str,
) -> List[Dict[str, object]]:
    groups: Dict[str, ConceptMapGroup] = {}
    for system_key, oo_code, snomed_code in mappings:
        oo_system_url = SYSTEM_URLS[system_key]
        if not oo_system_url:
            continue
        group_key: str = str(oo_system_url)
        if direction == "forward":
            source_url = group_key
            target_url = SNOMED_SYSTEM_URL
            element_code = oo_code
            target_code = snomed_code
        else:
            source_url = SNOMED_SYSTEM_URL
            target_url = group_key
            element_code = snomed_code
            target_code = oo_code

        if group_key not in groups:
            groups[group_key] = {
                "source": source_url,
                "target": target_url,
                "element": [],
            }
        group = groups[group_key]
        group["element"].append(
            {
                "code": element_code,
                "target": [
                    {
                        "code": target_code,
                        "relationship": "equivalent",
                    }
                ],
            }
        )

    for system_key in ("extraoral_3d", "intraoral_3d"):
        oo_system_url = SYSTEM_URLS[system_key]
        if not oo_system_url:
            continue
        group_key: str = str(oo_system_url)
        if group_key in groups:
            continue
        groups[group_key] = {
            "source": SNOMED_SYSTEM_URL if direction == "reverse" else group_key,
            "target": group_key if direction == "reverse" else SNOMED_SYSTEM_URL,
            "element": [],
        }

    return cast(List[Dict[str, object]], list(groups.values()))


class OrthodonticPhotographViewsConceptMap(ConceptMap):
    """Map Open Ortho photographic codes to SNOMED CT photographic concepts."""

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/ConceptMap/orthodontic-photograph-views"

    def __init__(self):
        url = self.static_url()
        super().__init__(
            url=url,
            version="0.1.0",
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
            group=_build_groups(PHOTO_VIEW_MAPPINGS, direction="forward"),
        )


class OrthodonticPhotographViewsReverseConceptMap(ConceptMap):
    """Map SNOMED CT photographic concepts to Open Ortho photographic codes."""

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/ConceptMap/orthodontic-photograph-views-reverse"

    def __init__(self):
        url = self.static_url()
        super().__init__(
            url=url,
            version="0.1.0",
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
            group=_build_groups(PHOTO_VIEW_MAPPINGS, direction="reverse"),
        )
