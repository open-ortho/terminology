from datetime import datetime

from terminology.fhir_types import ValueSet
from terminology.resources.naming_systems import OpenOrthoNamingSystem
from terminology.constants import VALUE_SET_UIDS

id = "dental-imaging"


class DentalImagingValueSet(ValueSet):
    """ValueSet of SNOMED CT procedure codes covering dental imaging modalities."""

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/ValueSet/{id}"

    def __init__(self):
        url = self.static_url()
        OPOR = OpenOrthoNamingSystem()
        contact = (OPOR.contact or [])[:1]
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{VALUE_SET_UIDS[id]}"
                }
            ],
            version="1.1.0",
            name="DentalImaging",
            title="Dental Imaging",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=OPOR.publisher,
            contact=contact,
            description="SNOMED CT procedure codes representing dental imaging modalities, "
                        "including radiography, photography, transillumination, and 3D scanning.",
            compose={
                "include": [
                    {
                        "system": "http://snomed.info/sct",
                        "concept": [
                            {
                                "code": "1293073005",
                                "display": "Plain X-ray cephalometry (procedure)"
                            },
                            {
                                "code": "105301000220109",
                                "display": "Plain X-ray cephalometry, lateral (procedure)"
                            },
                            {
                                "code": "241046008",
                                "display": "Dental plain X-ray bitewing (procedure)"
                            },
                            {
                                "code": "89846007",
                                "display": "Orthopantogram (procedure)"
                            },
                            {
                                "code": "1237138006",
                                "display": "Dental photography (procedure)"
                            },
                            {
                                "code": "309889005",
                                "display": "Transillumination of tooth (procedure)"
                            },
                            {
                                "code": "1357743003",
                                "display": "Three dimensional digital optical scan of oral cavity (procedure)"
                            },
                            {
                                "code": "371576000",
                                "display": "Video imaging procedure (procedure)"
                            },
                        ]
                    }
                ]
            }
        )


__all__ = ["DentalImagingValueSet"]
