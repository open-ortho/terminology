from datetime import datetime

from terminology.fhir_types import CodeSystem, CodeSystemConcept
from terminology.resources.naming_systems import CWRUOrthoNamingSystem
from terminology.resources.code_systems import leave_code_as_is as make_code
from terminology.constants import CODE_SYSTEM_UIDS


id = "cwru-ortho-record-type"


class CWRUOrthoRecordTypeCodeSystem(CodeSystem):  # Naming preserved for compatibility, but id now reflects record-type
    @classmethod
    def static_url(cls) -> str:
        ns = CWRUOrthoNamingSystem()
        return f"{ns.url}/CodeSystem/{id}"

    def __init__(self):
        ns = CWRUOrthoNamingSystem()
        super().__init__(
            id=id,
            identifier=[
                {
                    "system": "urn:ietf:rfc:3986",
                    "value": f"urn:oid:{CODE_SYSTEM_UIDS[id]}"
                }
            ],
            url=self.static_url(),
            version="1.0.0",
            name="CWRUOrthoRecordType",
            title="Bolton-Brush Growth Study Center Collection Record Types",
            status="active",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher=ns.publisher,
            description="Types for records which compose parts of longitudinal collections curated by the Bolton-Brush Growth Study Center at Case Western Reserve University.",
            caseSensitive=True,
            content="complete",
            concept=[
                CodeSystemConcept(
                    code=f"{make_code('L')}",
                    display="Lateral Cephalogram",
                    definition="Scan of Latero-Lateral (Sagittal) Cephalogram"
                ),
                CodeSystemConcept(
                    code=f"{make_code('F')}",
                    display="Frontal Cephalogram",
                    definition="Scan of Postero-Anterior (Coronal) Cephalogram"
                ),
                CodeSystemConcept(
                    code=f"{make_code('OB')}",
                    display="Oblique Cephalogram",
                    definition="Scan of Oblique Cephalogram"
                ),
                CodeSystemConcept(
                    code=f"{make_code('OC')}",
                    display="Occlusal Dental Plain Radiograph",
                    definition="Scan of Occlusal Dental Plain Radiograph"
                ),
                CodeSystemConcept(
                    code=f"{make_code('P')}",
                    display="Radiograph of Left Hip and Pelvis",
                    definition="Scan of Radiograph of Left Hip and Pelvis"
                ),
                CodeSystemConcept(
                    code=f"{make_code('FA')}",
                    display="Radiograph of Foot & Ankle",
                    definition="Scan of Radiograph of Foot & Ankle"
                ),
                CodeSystemConcept(
                    code=f"{make_code('H')}",
                    display="Radiograph of Hand & Wrist",
                    definition="Scan of Radiograph of Hand & Wrist"
                ),
                CodeSystemConcept(
                    code=f"{make_code('CS')}",
                    display="Radiograph of Left Shoulder and Chest",
                    definition="Scan of Radiograph of Left Shoulder and Chest"
                ),
                CodeSystemConcept(
                    code=f"{make_code('E')}",
                    display="Radiograph of Elbow",
                    definition="Scan of Radiograph of Elbow"
                ),
                CodeSystemConcept(
                    code=f"{make_code('K')}",
                    display="Radiograph of Left Knee",
                    definition="Scan of Radiograph of Left Knee"
                ),
                CodeSystemConcept(
                    code=f"{make_code('PH')}",
                    display="Photograph of Patient",
                    definition="Scan of Photograph of Patient"
                ),
                CodeSystemConcept(
                    code=f"{make_code('RE')}",
                    display="Record of Examination",
                    definition="Scan of Record of Examination"
                ),
                CodeSystemConcept(
                    code=f"{make_code('RF')}",
                    display="Record of Facial and Jaw Examination",
                    definition="Scan of Paper Record of Facial and Jaw Examination"
                ),
                CodeSystemConcept(
                    code=f"{make_code('RT')}",
                    display="Record of Cephalometric Tracing",
                    definition="Scan of Paper Record of Cephalometric Tracing"
                ),
                CodeSystemConcept(
                    code=f"{make_code('SM')}",
                    display="Complete Study Model",
                    definition="Scan of Complete (both Maxillary and Mandibular) Study Model"
                ),
                CodeSystemConcept(
                    code=f"{make_code('SU')}",
                    display="Upper Study Model",
                    definition="Scan of Study Model of the Maxillary (Upper) Dentition"
                ),
                CodeSystemConcept(
                    code=f"{make_code('SL')}",
                    display="Lower Study Model",
                    definition="Scan of Study Model of the Mandibular (Lower) Dentition"
                ),
                CodeSystemConcept(
                    code=f"{make_code('FM')}",
                    display="Facial Moulage",
                    definition="Scan of Facial Moulage"
                ),
                CodeSystemConcept(
                    code=f"{make_code('UK')}",
                    display="Unknown Record Type",
                    definition="Scan of Unknown Record Type"
                )
            ]
        )
