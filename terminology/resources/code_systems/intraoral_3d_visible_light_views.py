from fhir.resources.codesystem import CodeSystem, CodeSystemConcept
from datetime import datetime
from terminology.resources.naming_systems import OpenOrthoNamingSystem
from terminology.resources.code_systems import leave_code_as_is as make_code


class Intraoral3DVisibleLightViewsCodeSystem(CodeSystem):

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/intraoral-3d-visible-light-views"

    def __init__(self):
        OPOR = OpenOrthoNamingSystem()
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name=OPOR.name,
            title="Open-Ortho Code System",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="Open Ortho",
            description=OPOR.description,
            caseSensitive=True,
            content="complete",
            concept=[value for name, value in globals(
            ).items() if isinstance(value, CodeSystemConcept)]
        )


IV3D01 = CodeSystemConcept(
    code=f"{make_code('IV3D01')}",
    display="IV3D-01 IO.MX",
    definition="Intraoral 3D Surface of the Maxillary Dentition",
)

IV3D02 = CodeSystemConcept(
    code=f"{make_code('IV3D02')}",
    display="IV3D-02 IO.MD",
    definition="Intraoral 3D Surface of the Mandibular Dentition",
)

IV3D03 = CodeSystemConcept(
    code=f"{make_code('IV3D03')}",
    display="IV3D-03 IO.BT",
    definition="Intraoral 3D Surface of Occluding Maxillary and Mandibular Teeth (showing hot the teeth fir together, i.e. the bite)",
)
