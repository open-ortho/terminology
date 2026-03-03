from datetime import datetime

from terminology.fhir_types import ValueSet
from terminology.resources.naming_systems import CWRUOrthoNamingSystem
from terminology.resources.code_systems.cwru_ortho_image_types import (
    CWRUOrthoRecordTypeCodeSystem,
)
from terminology.constants import VALUE_SET_UIDS


id = "image-type-valueset"


class CWRUOrthoImageTypeValueSet(ValueSet):
    @classmethod
    def static_url(cls) -> str:
        ns = CWRUOrthoNamingSystem()
        return f"{ns.url}/{id}"

    def __init__(self):
        url = self.static_url()
        ns = CWRUOrthoNamingSystem()
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{VALUE_SET_UIDS[id]}"
                }
            ],
            version="1.0.0",
            name="CWRUOrthoImageTypes",
            title="CWRU Orthodontics Image Types",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=ns.publisher,
            description="Allowed CWRU Orthodontics image types for radiographic scans.",
            compose={
                "include": [
                    {"system": CWRUOrthoRecordTypeCodeSystem().url}
                ]
            }
        )
