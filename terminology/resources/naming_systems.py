from terminology.fhir_types import NamingSystem, Identifier
from terminology.constants import NAMING_SYSTEM_UIDS

class MedocoHealthNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/medoco",
            name="medocoHEALTH",
            title="medoco Health Naming System",
            identifier=[Identifier(
                system="dicom",
                value="99MDOC"
            )],
            description="""
## medoco Health Naming System by Dr. Marco Rosa 

A custom set of codes used by various medoco Health products, as reccommended by Dr. Marco Rosa.
""",
            status="draft",
            kind="codesystem",
            date="2025-01-01",
            publisher="medoco Health",
            responsible="medoco Health",
            uniqueId=[
                {
                    "type": "uri",
                    "value": "https://terminology.open-ortho.org/fhir/sid/medoco",
                    "preferred": True
                },
                {
                    "type": "oid",
                    "value": NAMING_SYSTEM_UIDS["medoco-health"],
                    "preferred": False
                },
                {
                    "type": "dicom",
                    "value": "99MDOC",
                    "preferred": True
                }
            ]
        )

class OpenOrthoNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/open-ortho",
            name="OpenOrtho",
            title="Open-Ortho",
            identifier=[Identifier(
                system="dicom",
                value="99OPOR"
            )],
            description="""
## OpenOrtho Naming System

A set of codes required to represent dental and orthodontic concepts for interoperability purposes, which are not yet available in other standard code systems.
""",
            status="draft",
            kind="codesystem",
            date="2025-01-01",
            publisher="OpenOrtho",
            responsible="OpenOrtho",
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
            uniqueId=[
                {
                    "type": "uri",
                    "value": "https://terminology.open-ortho.org/fhir/sid/open-ortho",
                    "preferred": False
                },
                {
                    "type": "oid",
                    "value": NAMING_SYSTEM_UIDS["open-ortho"],
                    "preferred": False
                },
                {
                    "type": "dicom",
                    "value": "99OPOR",
                    "preferred": True
                }
            ]
        )

class CWRUOrthoNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/cwru",
            name="CWRUOrtho",
            title="CWRU Orthodontics Naming System",
            identifier=[Identifier(
                system="dicom",
                value="99CWRU-ORTHO"
            )],
            description="""
## CWRU Orthodontics Naming System

Local coding scheme for radiographic imaging used at Case Western Reserve University Orthodontics.
""",
            status="draft",
            kind="codesystem",
            date="2025-01-01",
            publisher="CWRU Orthodontics",
            responsible="CWRU Orthodontics",
            uniqueId=[
                {
                    "type": "uri",
                    "value": "https://terminology.open-ortho.org/fhir/sid/cwru",
                    "preferred": True
                },
                {
                    "type": "oid",
                    "value": NAMING_SYSTEM_UIDS["cwru-ortho"],
                    "preferred": False
                },
                {
                    "type": "dicom",
                    "value": "99CWRU-ORTHO",
                    "preferred": False
                }
            ]
        )

class DentalEyePadNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/dentaleyepad",
            name="DentalEyePad",
            identifier=[Identifier(
                system="dicom",
                value="99DEYE"
            )],
            title="Dental Eyepad Naming System",
            description="""
# dentaleyepad image types

The dentaleyepad knows which images are to be taken and makes all the necessary image settings automatically. The photo assistant automatically displays the image types in the correct order.

This eliminates tedious intermediate steps such as connecting the camera, assigning patients and defining the image types.
""",
            status="draft",
            kind="codesystem",
            date="2024-12-30",
            publisher="doctorseyes GmbH",
            responsible="info@doctorseyes.de",
            uniqueId=[
                {
                    "type": "uri",
                    "value": "https://terminology.open-ortho.org/fhir/sid/dentaleyepad",
                    "preferred": True
                },
                {
                    "type": "oid",
                    "value": NAMING_SYSTEM_UIDS["dental-eye-pad"],
                    "preferred": False
                }
            ]
        )


class TopsorthoNamingSystem(NamingSystem):
    """NamingSystem for a specific topsOrtho server instance, identified by UUID.

    The UUID anonymously identifies the practice without leaking any identifying
    information. The DICOM coding scheme is derived from the UUID per the 99TOPS
    convention: 99TOPS + first 8 hex chars of the UUID (uppercase, no hyphens).
    """
    def __init__(self, uuid: str):
        dicom_scheme = f"99TOPS{uuid.replace('-', '').upper()[:8]}"
        url = f"https://terminology.open-ortho.org/fhir/sid/topsortho/{uuid}"
        super().__init__(
            url=url,
            name=f"TopsOrtho{uuid.replace('-', '').upper()[:8]}",
            title=f"topsOrtho Server Instance {uuid}",
            identifier=[Identifier(
                system="dicom",
                value=dicom_scheme
            )],
            description=(
                f"Codes from topsOrtho server instance {uuid}. "
                "These are practice-specific image label types defined locally "
                "on a specific topsOrtho server installation. The UUID identifies "
                "the server instance anonymously without revealing practice identity."
            ),
            status="active",
            kind="codesystem",
            date="2025-01-01",
            publisher="topsOrtho",
            responsible="topsOrtho",
            uniqueId=[
                {
                    "type": "uri",
                    "value": url,
                    "preferred": True
                },
                {
                    "type": "dicom",
                    "value": dicom_scheme,
                    "preferred": True
                }
            ]
        )
