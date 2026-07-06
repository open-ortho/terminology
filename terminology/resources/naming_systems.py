from terminology.fhir_types import NamingSystem, Identifier
from terminology.constants import NAMING_SYSTEM_UIDS, DICOM_UID_SYSTEM

class MedocoHealthNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/medoco",
            name="medocoHEALTH",
            title="medoco Health Naming System",
            identifier=[Identifier(
                system=DICOM_UID_SYSTEM,
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
                }
            ]
        )

class ADA1100NamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/ada1100",
            name="ADA1100",
            title="ANSI/ADA Standard No. 1100 Naming System",
            identifier=[Identifier(
                system=DICOM_UID_SYSTEM,
                value="99ADA1100"
            )],
            description="""
## ANSI/ADA Standard No. 1100 — Dental Informatics: Orthodontic Records

Codes defined in ANSI/ADA Standard No. 1100, hosted here by open-ortho on behalf
of the American Dental Association Standards Committee (SC).
The ADA does not operate a FHIR terminology server; open-ortho provides stable,
resolvable canonical URLs for these codes.
""",
            status="active",
            kind="codesystem",
            date="2025-01-01",
            publisher="American Dental Association",
            responsible="ADA Standards Committee",
            uniqueId=[
                {
                    "type": "uri",
                    "value": "https://terminology.open-ortho.org/fhir/sid/ada1100",
                    "preferred": True
                }
            ]
        )


class OpenOrthoNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir",
            name="OpenOrtho",
            title="Open-Ortho",
            identifier=[Identifier(
                system=DICOM_UID_SYSTEM,
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
                    "value": "https://terminology.open-ortho.org/fhir",
                    "preferred": False
                },
                {
                    "type": "oid",
                    "value": NAMING_SYSTEM_UIDS["open-ortho"],
                    "preferred": False
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
                system=DICOM_UID_SYSTEM,
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
                }
            ]
        )

class DentalEyePadNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="https://terminology.open-ortho.org/fhir/sid/dentaleyepad",
            name="DentalEyePad",
            identifier=[Identifier(
                system=DICOM_UID_SYSTEM,
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
                system=DICOM_UID_SYSTEM,
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
                }
            ]
        )


def get_dicom_identifier(ns: NamingSystem) -> str:
    """Return the DICOM coding scheme designator value from a NamingSystem's identifier list.

    Raises ValueError if no DICOM identifier is found.
    """
    for ident in (ns.identifier or []):
        if ident.system == DICOM_UID_SYSTEM:
            return ident.value
    raise ValueError(f"No DICOM identifier found in NamingSystem {ns.name!r}")
