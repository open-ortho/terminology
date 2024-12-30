from fhir.resources.valueset import ValueSet
from terminology.resources.code_systems.open_ortho_code_system import OrthodonticPhotographViewsCodeSystem

class OrthodonticPhotographViewsValueSet(ValueSet):
    """ Set of codes allowed for orthodontic photographs to be used in DICOM's ScheduledProtocol attribute. """
    @classmethod
    def static_url(cls) -> str:
        return "http://terminology.medoco.health/fhir/ValueSet/OrthodonticPhotographViews"

    def __init__(self):
        super().__init__(
            url=self.static_url(),
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": "urn:oid:1.3.6.1.4.1.62074.3.1"
                }
            ],
            version="0.1.0",
            name="Orthodontic Photographic Views",
            title="Orthodontic Photographic Views",
            status="active",
            experimental=False,
            date="2024-12-29",
            publisher="open-ortho",
            contact=[
                {
                    "name": "medoco Health",
                    "telecom": [
                        {
                            "system": "url",
                            "value": "https://medoco.health"
                        }
                    ]
                }
            ],
            description="A set of codes that describe Orhodontic Photographic Views for DICOM ",
            compose={
                "include": [
                    {
                        "system": OrthodonticPhotographViewsCodeSystem().url,
                        "concept": [
                            {"code": concept.code, "display": concept.display}
                            for concept in OrthodonticPhotographViewsCodeSystem().concept
                        ]
                    },
                    {
                        "system": "http://snomed.info/sct",
                        "filter": [
                            {
                                "property": "concept",
                                "op": "is-a",
                                "value": "723394009"
                            }
                        ]
                    }
                ]
            }
        )