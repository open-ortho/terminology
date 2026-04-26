""" This file defines ValueSets for specific subgroups of CWRU orthodontic
record types, categorized by material (acetate film, paper, gypsum).
"""
from datetime import datetime

from terminology.fhir_types import ValueSet
from terminology.resources.naming_systems import CWRUOrthoNamingSystem
from terminology.resources.code_systems.cwru_ortho_image_types import (
    CWRUOrthoRecordTypeCodeSystem,
)
from terminology.constants import VALUE_SET_UIDS

# ValueSets for subgroups

class CWRUOrthoRecordTypesAcetateFilm(ValueSet):
    @classmethod
    def static_url(cls) -> str:
        ns = CWRUOrthoNamingSystem()
        return f"{ns.url}/ValueSet/ortho-record-types-acetate-film"

    def __init__(self):
        url = self.static_url()
        ns = CWRUOrthoNamingSystem()
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{VALUE_SET_UIDS['ortho-record-types-acetate-film']}"
                }
            ],
            version="1.0.0",
            name="CWRUOrthoRecordTypesAcetateFilm",
            title="CWRU Ortho Record Types - Acetate Film",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=ns.publisher,
            description="Record types on acetate film for CWRU Bolton-Brush collections.",
            compose={
                "include": [
                    {
                        "system": CWRUOrthoRecordTypeCodeSystem().url,
                        "concept": [
                            {"code": code} for code in [
                                "L", "F", "OB", "OC", "P", "FA", "H", "CS", "E", "K"
                            ]
                        ]
                    }
                ]
            }
        )

class CWRUOrthoRecordTypesPaper(ValueSet):
    @classmethod
    def static_url(cls) -> str:
        ns = CWRUOrthoNamingSystem()
        return f"{ns.url}/ValueSet/ortho-record-types-paper"

    def __init__(self):
        url = self.static_url()
        ns = CWRUOrthoNamingSystem()
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{VALUE_SET_UIDS['ortho-record-types-paper']}"
                }
            ],
            version="1.0.0",
            name="CWRUOrthoRecordTypesPaper",
            title="CWRU Ortho Record Types - Paper Records",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=ns.publisher,
            description="Paper-based record types for CWRU Bolton-Brush collections.",
            compose={
                "include": [
                    {
                        "system": CWRUOrthoRecordTypeCodeSystem().url,
                        "concept": [
                            {"code": code} for code in ["RE", "RF"]
                        ]
                    }
                ]
            }
        )

class CWRUOrthoRecordTypesGypsum(ValueSet):
    @classmethod
    def static_url(cls) -> str:
        ns = CWRUOrthoNamingSystem()
        return f"{ns.url}/ValueSet/ortho-record-types-gypsum"

    def __init__(self):
        url = self.static_url()
        ns = CWRUOrthoNamingSystem()
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{VALUE_SET_UIDS['ortho-record-types-gypsum']}"
                }
            ],
            version="1.0.0",
            name="CWRUOrthoRecordTypesGypsum",
            title="CWRU Ortho Record Types - Gypsum Models",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=ns.publisher,
            description="Gypsum study model types for CWRU Bolton-Brush collections.",
            compose={
                "include": [
                    {
                        "system": CWRUOrthoRecordTypeCodeSystem().url,
                        "concept": [
                            {"code": code} for code in ["SM", "SU", "SL", "FM"]
                        ]
                    }
                ]
            }
        )
