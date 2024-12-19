from fhir.resources.namingsystem import NamingSystem


class MarcoRosaNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__()
        self.url = "http://marcorosa.it/fhir"
        self.name = "RSOMRC"
        self.title = "Dr. Marco Rosa Naming System"
        self.description = """
## Dr. Marco Rosa Naming System
 
A custom set of codes used in the practice of Dr. Marco Rosa, which may or may not have equivalents in other standard code systems.
"""
        self.status = "draft"
        self.kind = "codesystem"
        self.date = "2025-01-01"
        self.publisher = "Dr. Marco Rosa"
        self.responsible = "medoco Health"
        self.uniqueId = [
            {
                "type": "uuid",
                "value": "1.3.6.1.4.1.62074.3.1",
                "preferred": True
            }
        ]

class OpenOrthoNamingSystem(NamingSystem):
    def __init__(self):
        super().__init__()
        self.url = "http://open-ortho.org/terminology/fhir"
        self.name = "OPOR"
        self.title = "Open-Ortho Naming System"
        self.description = """
## OpenOrtho Naming System
 
A set of codes required to represents dental and orthodontic concepts for interoperability purposes, which are not yet available in other standard code systems.
"""
        self.status = "draft"
        self.kind = "codesystem"
        self.date = "2021-01-01"
        self.publisher = "OpenOrtho"
        self.responsible = "OpenOrtho"
        self.uniqueId = [
            {
                "type": "uuid",
                "value": "1.3.6.1.4.1.61741.11.3",
                "preferred": True
            }
        ]
