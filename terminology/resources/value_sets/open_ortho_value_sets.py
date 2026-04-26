"""ValueSets that combine Open Ortho and SNOMED CT photographic concepts.

This module defines FHIR ValueSets that include local Open Ortho CodeSystems and
SNOMED CT concept filters. The ValueSet definitions are static and can be built
into JSON artifacts, but expansion of SNOMED filters requires an external
terminology server.
"""

from terminology.fhir_types import ValueSet
from terminology.resources.code_systems.extraoral_2d_photographic_scheduled_protocol import (
    Extraoral2DPhotographicScheduledProtocolCodeSystem,
)


class OrthodonticPhotographViewsValueSet(ValueSet):
    """ValueSet combining Open Ortho extraoral 2D codes with SNOMED CT concepts.

    Produces a FHIR ValueSet that includes the Open Ortho CodeSystem and a SNOMED
    CT `is-a` filter rooted at concept `723394009` (Photographic image record).
    The definition is static; SNOMED expansion is expected to be performed by a
    terminology server rather than this codebase.
    """
    @classmethod
    def static_url(cls) -> str:
        return "https://terminology.open-ortho.org/fhir/sid/open-ortho/ValueSet/OrthodonticPhotographViews"

    def __init__(self):
        url = self.static_url()
        super().__init__(
            url=url,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": "urn:oid:1.2.840.10008.2.16.4"
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
                    "name": "Open-Ortho",
                    "telecom": [
                        {
                            "system": "url",
                            "value": "https://open-ortho.org"
                        }
                    ]
                }
            ],
            description="A set of codes that describe Orhodontic Photographic Views for DICOM ",
            compose={
                "include": [
                    {
                        "system": Extraoral2DPhotographicScheduledProtocolCodeSystem().url,
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
