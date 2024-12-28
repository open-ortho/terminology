from fhir.resources.valueset import ValueSet
from terminology.resources.code_systems.open_ortho_code_system import OpenOrthoCodeSystem

class DicomScheduledProtocol(ValueSet):
    """ Set of codes allowed for orthodontic photographs to be used in DICOM's ScheduledProtocol attribute. """
    @classmethod
    def static_url(cls) -> str:
        return "http://dicom.nema.org/resources/ontology/DCM"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": "urn:oid:1.2.840.10008.2.16.4"
                }
            ],
            version="2021-11-01",
            name="DICOM Scheduled Protocol",
            title="DICOM Scheduled Protocol",
            status="active",
            experimental=False,
            date="2021-11-01",
            publisher="NEMA",
            contact=[
                {
                    "name": "DICOM Standards Committee",
                    "telecom": [
                        {
                            "system": "url",
                            "value": "http://dicom.nema.org"
                        }
                    ]
                }
            ],
            description="A set of codes for DICOM Scheduled Protocols",
            compose={
                "include": [
                    {
                        "system": OpenOrthoCodeSystem().url,
                        "concept": [
                            {"code": concept.code, "display": concept.display}
                            for concept in OpenOrthoCodeSystem().concept
                        ]
                    }
                ]
            }
        )