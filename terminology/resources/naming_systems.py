from fhir.resources.namingsystem import NamingSystem

class MarcoRosaNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="http://marcorosa.it/fhir",
            name="RSOMRC",
            title="Dr. Marco Rosa Naming System",
            description="""
## Dr. Marco Rosa Naming System

A custom set of codes used in the practice of Dr. Marco Rosa, which may or may not have equivalents in other standard code systems.
""",
            status="draft",
            kind="codesystem",
            date="2025-01-01",
            publisher="Dr. Marco Rosa",
            responsible="medoco Health",
            uniqueId=[
                {
                    "type": "uuid",
                    "value": "1.3.6.1.4.1.62074.3.1",
                    "preferred": True
                }
            ]
        )

class OpenOrthoNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__(
            url="http://open-ortho.org/terminology/fhir",
            name="OPOR",
            title="Open-Ortho Naming System",
            description="""
## OpenOrtho Naming System

A set of codes required to represent dental and orthodontic concepts for interoperability purposes, which are not yet available in other standard code systems.
""",
            status="draft",
            kind="codesystem",
            date="2021-01-01",
            publisher="OpenOrtho",
            responsible="OpenOrtho",
            uniqueId=[
                {
                    "type": "uuid",
                    "value": "1.3.6.1.4.1.62074.3.1",
                    "preferred": True
                }
            ]
        )