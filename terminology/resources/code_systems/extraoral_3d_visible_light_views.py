from fhir.resources.codesystem import CodeSystem, CodeSystemConcept
from datetime import datetime
from terminology.resources.naming_systems import OpenOrthoNamingSystem
from terminology.resources.code_systems import leave_code_as_is as make_code


class Extraoral3DPhotographicViewsCodeSystem(CodeSystem):

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/extraoral-3d-photographic-views"

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


EV3D01 = CodeSystemConcept(
    code=f"{make_code('EV3D01')}",
    display="EV3D-01 EO.WH.LC.CO",
    definition="Whole head, lips closed, centric occlusion",
)

EV3D02 = CodeSystemConcept(
    code=f"{make_code('EV3D02')}",
    display="EV3D-02 EO.WH.LC.CR",
    definition="Whole head, lips closed, centric relation",
)

EV3D03 = CodeSystemConcept(
    code=f"{make_code('EV3D03')}",
    display="EV3D-03 EO.WH.LR.CO",
    definition="Whole head, lips relaxed, centric occlusion",
)

EV3D04 = CodeSystemConcept(
    code=f"{make_code('EV3D04')}",
    display="EV3D-04 EO.WH.LR.CR",
    definition="Whole head, lips relaxed, centric relation",
)

EV3D05 = CodeSystemConcept(
    code=f"{make_code('EV3D05')}",
    display="EV3D-05 EO.WH.FS.CO",
    definition="Whole head, full smile, centric occlusion",
)

EV3D06 = CodeSystemConcept(
    code=f"{make_code('EV3D06')}",
    display="EV3D-06 EO.WH.FS.CR",
    definition="Whole head, full smile, centric relation",
)
