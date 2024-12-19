from fhir.resources.valueset import ValueSet
from terminology.terminology.code_systems.open_ortho_code_system import OpenOrthoCodeSystem

class DicomScheduledProtocol(ValueSet):
    """ Set of codes allowed for orthodontic photographs to be used in DICOM's ScheduledProtocol attribute. """
    def __init__(self):
        super().__init__()
        self.url = "http://dicom.nema.org/resources/ontology/DCM"
        self.identifier = [
            {
                "system": "urn:ietf:rfc:3986",
                "value": "urn:oid:1.2.840.10008.2.16.4"
            }
        ]
        self.version = "2021-11-01"
        self.name = "DICOM Scheduled Protocol"
        self.title = "DICOM Scheduled Protocol"
        self.status = "active"
        self.experimental = False
        self.date = "2021-11-01"
        self.publisher = "NEMA"
        self.contact = [
            {
                "name": "DICOM Standards Committee",
                "telecom": [
                    {
                        "system": "url",
                        "value": "http://dicom.nema.org"
                    }
                ]
            }
        ]
        self.description = "A set of codes for DICOM Scheduled Protocols"

        # Include codes from OpenOrthoCodeSystem
        ortho_code_system = OpenOrthoCodeSystem()
        self.compose = {
            "include": [
                {
                    "system": ortho_code_system.url,
                    "concept": [
                        {"code": concept.code, "display": concept.display}
                        for concept in ortho_code_system.concept
                    ]
                }
            ]
        }