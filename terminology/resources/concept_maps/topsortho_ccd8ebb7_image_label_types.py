"""ConceptMaps linking topsOrtho CCD8EBB7 image label types to standard codes.

Each class inherits :class:`~terminology.resources.concept_maps.base.MappedConceptMap`
and shares the same ``MAPPINGS`` list.  The forward map goes topsOrtho → (SNOMED CT
and/or ADA-1100 protocol codes); the reverse map swaps source and target for each
group.  Both are built automatically by ``_build_groups()``.

The ``MAPPINGS`` list covers three target systems:

- ``http://snomed.info/sct`` — imaging procedure codes (radiography, photography,
  video, transillumination)
- ADA-1100 intraoral 2D scheduled-protocol codes
- ADA-1100 extraoral 2D scheduled-protocol codes
"""

from datetime import datetime

from terminology.resources.concept_maps.base import MappedConceptMap, MappingEntry
from terminology.resources.naming_systems import TopsorthoNamingSystem
from terminology.resources.code_systems.topsortho_ccd8ebb7_image_label_types import (
    TopsorthoCCD8EBB7ImageLabelTypesCodeSystem,
)
from terminology.resources.code_systems.ada_1100_intraoral_2d_photographic_scheduled_protocol import (
    Intraoral2DPhotographicScheduledProtocolCodeSystem,
)
from terminology.resources.code_systems.ada_1100_extraoral_2d_photographic_scheduled_protocol import (
    Extraoral2DPhotographicScheduledProtocolCodeSystem,
)


_PRACTICE_UUID = "CCD8EBB7-5A23-40B9-A8A7-AD3D6D14C4FE"
SNOMED_SYSTEM_URL = "http://snomed.info/sct"

_SRC = TopsorthoCCD8EBB7ImageLabelTypesCodeSystem.static_url()
_IV = Intraoral2DPhotographicScheduledProtocolCodeSystem.static_url()
_EV = Extraoral2DPhotographicScheduledProtocolCodeSystem.static_url()

_E = MappingEntry  # local alias for brevity


class TopsorthoCCD8EBB7ImageLabelTypesConceptMap(MappedConceptMap):
    """Map topsOrtho CCD8EBB7 image label types to SNOMED CT and ADA-1100 codes.

    Source system is the topsOrtho CCD8EBB7 image-label-types CodeSystem.
    Target systems are SNOMED CT (procedure codes) and the ADA-1100 intraoral
    and extraoral 2D scheduled-protocol CodeSystems.

    Relationships include ``equivalent``, ``inexact``, and ``wider`` to capture
    the varying degrees of semantic match between practice-specific labels and
    standard terminology.
    """

    MAPPINGS = [
        # ── SNOMED: radiography ───────────────────────────────────────────────
        _E(_SRC, "1",    SNOMED_SYSTEM_URL, "1293073005",     "equivalent",
           "TELE P-A",           "Plain X-ray cephalometry (procedure)",          ""),
        _E(_SRC, "2",    SNOMED_SYSTEM_URL, "1293073005",     "inexact",    "Tracciato TELE P-A",
           "Plain X-ray cephalometry (procedure)",          "With Cephaloemtric Tracing"),
        _E(_SRC, "9",    SNOMED_SYSTEM_URL, "105301000220109", "equivalent",
           "TELE",               "Plain X-ray cephalometry, lateral (procedure)", ""),
        _E(_SRC, "10",   SNOMED_SYSTEM_URL, "105301000220109", "inexact",    "Tracciato TELE",
           "Plain X-ray cephalometry, lateral (procedure)", "With Cephaloemtric Tracing"),
        _E(_SRC, "18",   SNOMED_SYSTEM_URL, "89846007",       "equivalent",
           "OPT",                "Orthopantogram (procedure)",                    ""),
        _E(_SRC, "35",   SNOMED_SYSTEM_URL, "371576000",      "equivalent",
           "5 video",            "Video imaging procedure (procedure)",           ""),
        _E(_SRC, "5007", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RX1",                "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5056", SNOMED_SYSTEM_URL, "309889005",      "equivalent", "DK",
           "Transillumination of tooth (procedure)",        ""),
        _E(_SRC, "5076", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE1",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5077", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE2",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5078", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE3",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5079", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE4",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5080", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE5",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5081", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE6",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5082", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE7",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5083", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE8",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5084", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE9",               "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5085", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE10",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5086", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE11",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5087", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE12",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5088", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE13",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5089", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE14",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5090", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE15",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5091", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE16",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5092", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE21",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5093", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE17",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5094", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE18",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5095", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE19",              "Dental plain X-ray bitewing (procedure)",       ""),
        _E(_SRC, "5096", SNOMED_SYSTEM_URL, "241046008",      "equivalent",
           "RXE20",              "Dental plain X-ray bitewing (procedure)",       ""),
        # ── SNOMED: photography & video ──────────────────────────────────────
        _E(_SRC, "5098", SNOMED_SYSTEM_URL, "1237138006",     "equivalent",
           "PL DIGA 4",          "Dental photography (procedure)",                ""),
        _E(_SRC, "5102", SNOMED_SYSTEM_URL, "371576000",      "equivalent",
           "video 1",            "Video imaging procedure (procedure)",           ""),
        _E(_SRC, "5103", SNOMED_SYSTEM_URL, "371576000",      "equivalent",
           "video 2",            "Video imaging procedure (procedure)",           ""),
        _E(_SRC, "5104", SNOMED_SYSTEM_URL, "371576000",      "equivalent",
           "video 3",            "Video imaging procedure (procedure)",           ""),
        _E(_SRC, "5111", SNOMED_SYSTEM_URL, "1237138006",     "wider",
           "PL sorriso da sopra", "Dental photography (procedure)",                ""),
        _E(_SRC, "5112", SNOMED_SYSTEM_URL, "1237138006",     "wider",
           "PL 5 MIP  TQ dx",   "Dental photography (procedure)",                ""),
        _E(_SRC, "5113", SNOMED_SYSTEM_URL, "1237138006",     "wider",
           "PL 5 MIP TQ sx",    "Dental photography (procedure)",                ""),
        _E(_SRC, "5114", SNOMED_SYSTEM_URL, "1237138006",     "wider",
           "PL 5 P 2+2",        "Dental photography (procedure)",                ""),
        # ── Intraoral 2D ─────────────────────────────────────────────────────
        _E(_SRC, "4",    _IV, "IV18", "equivalent", "6 MIP",
           "Intraoral photo,left buccal,centric occl.,no mirror",             ""),
        _E(_SRC, "5",    _IV, "IV18", "inexact",    "STL 6",   "Intraoral photo,left buccal,centric occl.,no mirror",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "11",   _IV, "IV27", "equivalent", "8",
           "Intraoral photo,mandibular,mouth open,occlusal,mirror,corrected", ""),
        _E(_SRC, "14",   _IV, "IV25", "equivalent", "7",
           "Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",  ""),
        _E(_SRC, "19",   _IV, "IV01", "equivalent", "4 MIP",
           "Intraoral photo,right buccal,centric occl.,no mirror",            ""),
        _E(_SRC, "20",   _IV, "IV01", "inexact",    "STL 4",   "Intraoral photo,right buccal,centric occl.,no mirror",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "31",   _IV, "IV07", "equivalent", "5 MIP",
           "Intraoral photo,frontal,centric occl.,no mirror",                 ""),
        _E(_SRC, "32",   _IV, "IV07", "inexact",    "STL 5",   "Intraoral photo,frontal,centric occl.,no mirror",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "5014", _IV, "IV09", "equivalent", "5 BA",
           "Intraoral photo,frontal,teeth apart,no mirror",                   ""),
        _E(_SRC, "5025", _IV, "IV08", "equivalent", "5 CO",
           "Intraoral photo,frontal,centric relation,no mirror",              ""),
        _E(_SRC, "5026", _IV, "IV21", "equivalent", "6 CO",
           "Intraoral photo,left buccal,centric relation,no mirror",          ""),
        _E(_SRC, "5028", _IV, "IV04", "equivalent", "4 CO",
           "Intraoral photo,right buccal,centric relation,no mirror",         ""),
        _E(_SRC, "5034", _IV, "IV11", "inexact",    "9 MIP",
           "Intraoral photo,front view inferior,centric occl.,no mirror",     ""),
        _E(_SRC, "5051", _IV, "IV12", "inexact",    "9 CO",
           "Intraoral photo,front view inferior,centric relation,no mirror",  ""),
        _E(_SRC, "5099", _IV, "IV25", "inexact",    "STL 7",   "Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "5100", _IV, "IV27", "inexact",    "STL 8",   "Intraoral photo,mandibular,mouth open,occlusal,mirror,corrected",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "5101", _IV, "IV11", "inexact",    "STL 9",   "Intraoral photo,front view inferior,centric occl.,no mirror",
           "View of 3D Digital Optical Surface Scan Rendering"),
        _E(_SRC, "5115", _IV, "IV28", "inexact",    "RS sonda 1",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5116", _IV, "IV28", "inexact",    "RS sonda 2",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5117", _IV, "IV28", "inexact",    "RS sonda 3",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5118", _IV, "IV28", "inexact",    "RS sonda 4",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5119", _IV, "IV28", "inexact",    "RS sonda 5",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5120", _IV, "IV28", "inexact",    "RS sonda 6",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5121", _IV, "IV28", "inexact",    "RS sonda 7",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5122", _IV, "IV28", "inexact",    "RS sonda 8",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5123", _IV, "IV28", "inexact",    "RS sonda 9",  "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5124", _IV, "IV28", "inexact",    "RS sonda 10", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5125", _IV, "IV28", "inexact",    "RS sonda 11", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5126", _IV, "IV28", "inexact",    "RS sonda 12", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5127", _IV, "IV28", "inexact",    "RS sonda 13", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5128", _IV, "IV28", "inexact",    "RS sonda 14", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5129", _IV, "IV28", "inexact",    "RS sonda 15", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5130", _IV, "IV28", "inexact",    "RS sonda 16", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5131", _IV, "IV28", "inexact",    "RS sonda 17", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        _E(_SRC, "5132", _IV, "IV28", "inexact",    "RS sonda 18", "Intraoral photo,gingival recession",
           "With 462735007,SCT,Periodontal probe (physical object)"),
        # ── Extraoral 2D ─────────────────────────────────────────────────────
        _E(_SRC, "6",    _EV, "EV03", "equivalent", "1 MIP labbra rilassate",
           "Extraoral photo,right profile,lips closed,centric occlusion",    ""),
        _E(_SRC, "29",   _EV, "EV19", "equivalent", "3",
           "Extraoral photo,full face,full smile,centric occlusion",          ""),
        _E(_SRC, "30",   _EV, "EV17", "equivalent", "2 MIP labbra rilassate",
           "Extraoral photo,full face,lips closed,centric occlusion",         ""),
        _E(_SRC, "34",   _EV, "EV17", "inexact",    "2 foto/tracciato",
           "Extraoral photo,full face,lips closed,centric occlusion",         "With Cephaloemtric Tracing"),
        _E(_SRC, "5002", _EV, "EV39", "equivalent", "Legnetto PO",
           "Extraoral photo,other face,occlusal cant",                        ""),
        _E(_SRC, "5003", _EV, "EV16", "equivalent", "1 RO",
           "Extraoral photo,full face,lips relaxed,centric relation",         ""),
        _E(_SRC, "5004", _EV, "EV36", "inexact",    "2 SUB7",
           "Extraoral photo,other face,inferior view",                        ""),
        _E(_SRC, "5005", _EV, "EV16", "equivalent", "2 RO",
           "Extraoral photo,full face,lips relaxed,centric relation",         ""),
        _E(_SRC, "5006", _EV, "EV06", "equivalent", "1 S",
           "Extraoral photo,right profile,full smile,centric relation",       ""),
        _E(_SRC, "5017", _EV, "EV36", "equivalent", "2 SV",
           "Extraoral photo,other face,inferior view",                        ""),
        _E(_SRC, "5018", _EV, "EV17", "equivalent", "2 P",
           "Extraoral photo,full face,lips closed,centric occlusion",         "Close-up"),
        _E(_SRC, "5019", _EV, "EV38", "equivalent", "3 P",
           "Extraoral photo,other face,close-up smile",                       ""),
        _E(_SRC, "5020", _EV, "EV16", "equivalent", "2 P RO",
           "Extraoral photo,full face,lips relaxed,centric relation",         "Close-up"),
        _E(_SRC, "5029", _EV, "EV20", "equivalent", "3 BA",
           "Extraoral photo,full face,full smile,centric relation",           ""),
        _E(_SRC, "5031", _EV, "EV18", "equivalent", "2 CO",
           "Extraoral photo,full face,lips closed,centric relation",          ""),
        _E(_SRC, "5037", _EV, "EV23", "equivalent", "1 RO sx",
           "Extraoral photo,left profile,lips relaxed,centric relation",      ""),
        _E(_SRC, "5038", _EV, "EV22", "equivalent", "1 sx",
           "Extraoral photo,left profile,lips relaxed,centric occlusion",     ""),
        _E(_SRC, "5039", _EV, "EV27", "equivalent", "1 S sx",
           "Extraoral photo,left profile,full smile,centric relation",        ""),
        _E(_SRC, "5042", _EV, "EV27", "equivalent", "3 P sx",
           "Extraoral photo,left profile,full smile,centric relation",        "Close-up"),
        _E(_SRC, "5043", _EV, "EV06", "equivalent", "3 P dx",
           "Extraoral photo,right profile,full smile,centric relation",       "Close-up"),
        _E(_SRC, "5044", _EV, "EV06", "inexact",    "3 P BA",
           "Extraoral photo,right profile,full smile,centric relation",       "Close-up, Teeth-Apart lower incisor visible"),
        _E(_SRC, "5046", _EV, "EV09", "equivalent", "3/4 dx RO ",
           "Extraoral photo,right profile 45,lips relaxed,centric relation",  ""),
        _E(_SRC, "5047", _EV, "EV30", "equivalent", "3/4 sx RO ",
           "Extraoral photo,left profile 45,lips relaxed,centric relation",   ""),
        _E(_SRC, "5050", _EV, "EV16", "equivalent", "2 P BA",
           "Extraoral photo,full face,lips relaxed,centric relation",         "Close-up, Teeth-Apart lower incisor visible"),
        _E(_SRC, "5057", _EV, "EV31", "equivalent", "3/4 sx",
           "Extraoral photo,left profile 45,lips closed,centric occlusion",   ""),
        _E(_SRC, "5058", _EV, "EV10", "equivalent", "3/4 dx",
           "Extraoral photo,right profile 45,lips closed,centric occlusion",  ""),
        _E(_SRC, "5059", _EV, "EV13", "equivalent", "3/4 S dx",
           "Extraoral photo,right profile 45,full smile,centric relation",    ""),
        _E(_SRC, "5060", _EV, "EV34", "equivalent", "3/4 S sx",
           "Extraoral photo,left profile 45,full smile,centric relation",     ""),
        _E(_SRC, "5061", _EV, "EV04", "equivalent", "1 CO",
           "Extraoral photo,right profile,lips closed,centric relation",      ""),
        _E(_SRC, "5064", _EV, "EV38", "inexact",    "2 P fonazione 1",
           "Extraoral photo,other face,close-up smile",                       "While Speaking"),
        _E(_SRC, "5065", _EV, "EV38", "inexact",    "2 P fonazione 2",
           "Extraoral photo,other face,close-up smile",                       "While Speaking"),
        _E(_SRC, "5066", _EV, "EV38", "inexact",    "2 P fonazione 3",
           "Extraoral photo,other face,close-up smile",                       "While Speaking"),
        _E(_SRC, "5097", _EV, "EV38", "equivalent", "PL 2 P social smile",
           "Extraoral photo,other face,close-up smile",                       ""),
        _E(_SRC, "5107", _EV, "EV03", "inexact",    "PL 1 P dx",
           "Extraoral photo,right profile,lips closed,centric occlusion",     "Close-Up"),
        _E(_SRC, "5108", _EV, "EV02", "inexact",    "PL 1 P RO dx",
           "Extraoral photo,right profile,lips relaxed,centric relation",     "Close-Up"),
        _E(_SRC, "5109", _EV, "EV06", "inexact",    "PL 1 S P social smile dx",
           "Extraoral photo,right profile,full smile,centric relation",       "Close-Up"),
        _E(_SRC, "5110", _EV, "EV06", "inexact",    "PL 1 S P full smile dx",
           "Extraoral photo,right profile,full smile,centric relation",       "Close-Up"),
        _E(_SRC, "5133", _EV, "EV24", "inexact",    "1 P sx",
           "Extraoral photo,left profile,lips closed,centric occlusion",      "Close-Up"),
        _E(_SRC, "5134", _EV, "EV23", "inexact",    "1 P RO sx",
           "Extraoral photo,left profile,lips relaxed,centric relation",      "Close-Up"),
        _E(_SRC, "5135", _EV, "EV27", "inexact",    "1 P S sx",
           "Extraoral photo,left profile,full smile,centric relation",        "Close-Up"),
        _E(_SRC, "5139", _EV, "EV38", "equivalent", "PL 2 P  full smile",
           "Extraoral photo,other face,close-up smile",                       ""),
    ]

    @classmethod
    def static_url(cls) -> str:
        return f"{TopsorthoNamingSystem(_PRACTICE_UUID).url}/ConceptMap/image-label-types"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name="TopsorthoCCD8EBB7ImageLabelTypesConceptMap",
            title="topsOrtho CCD8EBB7 Image Label Types ConceptMap",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="OpenOrtho",
            description=(
                "Mapping from topsOrtho server CCD8EBB7 image label types to "
                "SNOMED CT procedure codes and ADA-1100 scheduled protocol codes."
            ),
            sourceScopeUri=_SRC,
            group=self._build_groups(direction="forward"),
        )


class TopsorthoCCD8EBB7ImageLabelTypesReverseConceptMap(MappedConceptMap):
    """Reverse map: SNOMED CT and ADA-1100 codes → topsOrtho CCD8EBB7 image label types.

    Shares ``MAPPINGS`` with
    :class:`TopsorthoCCD8EBB7ImageLabelTypesConceptMap`; groups are built with
    ``direction="reverse"`` so source and target are swapped.  Asymmetric
    relationships are inverted automatically (``wider`` ↔ ``narrower``).
    """

    MAPPINGS = TopsorthoCCD8EBB7ImageLabelTypesConceptMap.MAPPINGS

    @classmethod
    def static_url(cls) -> str:
        return f"{TopsorthoNamingSystem(_PRACTICE_UUID).url}/ConceptMap/image-label-types-reverse"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name="TopsorthoCCD8EBB7ImageLabelTypesReverseConceptMap",
            title="topsOrtho CCD8EBB7 Image Label Types Reverse ConceptMap",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="OpenOrtho",
            description=(
                "Reverse mapping from SNOMED CT procedure codes and ADA-1100 "
                "scheduled protocol codes to topsOrtho server CCD8EBB7 image label types."
            ),
            targetScopeUri=_SRC,
            group=self._build_groups(direction="reverse"),
        )


__all__ = [
    "TopsorthoCCD8EBB7ImageLabelTypesConceptMap",
    "TopsorthoCCD8EBB7ImageLabelTypesReverseConceptMap",
]
