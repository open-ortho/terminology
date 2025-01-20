from fhir.resources.codesystem import CodeSystem, CodeSystemConcept, CodeSystemConceptDesignation
from datetime import datetime
from terminology.resources.naming_systems import OpenOrthoNamingSystem
from terminology.resources.code_systems import leave_code_as_is as make_code
from terminology.resources.code_systems import add_meta_to_resource

id = "intraoral-2d-photographic-scheduled-protocol"

class Intraoral2DPhotographicScheduledProtocolCodeSystem(CodeSystem):

    @classmethod
    def static_url(cls) -> str:
        ns = OpenOrthoNamingSystem()
        return f"{ns.url}/{id}"

    def __init__(self):
        OPOR = OpenOrthoNamingSystem()
        super().__init__(
            id=id,
            identifier=OPOR.identifier,
            url=self.static_url(),
            version="1.2.0",
            name="Intraoral2DPhotographicScheduledProtocol",
            title="Intraoral 2D Photographic Scheduled Protocol",
            status="draft",
            experimental=False,
            date=datetime.now().date().isoformat(),
            publisher="Open Ortho",
            description="Common intraoral 2D photographic views used in an orthodontic provider's practice",
            caseSensitive=True,
            content="complete",
            concept=[value for name, value in globals(
            ).items() if isinstance(value, CodeSystemConcept)]
        )


IV01 = CodeSystemConcept(
    code=f"{make_code('IV01')}",
    display="Intraoral photo, right buccal, centric occlusion",
    definition="Intraoral Right Buccal Segment, Centric Occlusion, Direct View",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-01",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.RB.CO",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV02 = CodeSystemConcept(
    code=f"{make_code('IV02')}",
    display="Intraoral photo, right buccal, centric occlusion, with mirror",
    definition="Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-02",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.RB.CO.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV03 = CodeSystemConcept(
    code=f"{make_code('IV03')}",
    display="Intraoral photo,right buccal,centric occlusion,mirror,corrected",
    definition="Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-03",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.RB.CO.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV04 = CodeSystemConcept(
    code=f"{make_code('IV04')}",
    display="Intraoral photo, left buccal, centric occlusion",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, Direct View",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-04",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.LB.CO",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV05 = CodeSystemConcept(
    code=f"{make_code('IV05')}",
    display="Intraoral photo, left buccal, centric occlusion, with mirror",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-05",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.LB.CO.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV06 = CodeSystemConcept(
    code=f"{make_code('IV06')}",
    display="Intraoral photo,left buccal,centric occlusion,mirror,corrected",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-06",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.LB.CO.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV07 = CodeSystemConcept(
    code=f"{make_code('IV07')}",
    display="Intraoral photo, anterior occlusal",
    definition="Intraoral, Anterior Occlusal, Direct View",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-07",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.AO",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV08 = CodeSystemConcept(
    code=f"{make_code('IV08')}",
    display="Intraoral photo, anterior occlusal, with mirror",
    definition="Intraoral, Anterior Occlusal, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-08",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.AO.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV09 = CodeSystemConcept(
    code=f"{make_code('IV09')}",
    display="Intraoral photo, anterior occlusal, mirror, corrected",
    definition="Intraoral, Anterior Occlusal, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-09",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.AO.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV10 = CodeSystemConcept(
    code=f"{make_code('IV10')}",
    display="Intraoral photo, mandibular, mouth open, occlusal view",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-10",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MD.MO.OV",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV11 = CodeSystemConcept(
    code=f"{make_code('IV11')}",
    display="Intraoral photo, mandibular, mouth open, occlusal view, mirror",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-11",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MD.MO.OV.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV12 = CodeSystemConcept(
    code=f"{make_code('IV12')}",
    display="Intraoral photo,mandibular,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-12",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MD.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV13 = CodeSystemConcept(
    code=f"{make_code('IV13')}",
    display="Intraoral photo, maxillary, mouth open, occlusal view",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-13",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV14 = CodeSystemConcept(
    code=f"{make_code('IV14')}",
    display="Intraoral photo, maxillary, mouth open, occlusal view, mirror",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-14",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV15 = CodeSystemConcept(
    code=f"{make_code('IV15')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-15",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV16 = CodeSystemConcept(
    code=f"{make_code('IV16')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-16",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV17 = CodeSystemConcept(
    code=f"{make_code('IV17')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-17",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV18 = CodeSystemConcept(
    code=f"{make_code('IV18')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-18",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV19 = CodeSystemConcept(
    code=f"{make_code('IV19')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-19",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV20 = CodeSystemConcept(
    code=f"{make_code('IV20')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-20",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV21 = CodeSystemConcept(
    code=f"{make_code('IV21')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-21",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV22 = CodeSystemConcept(
    code=f"{make_code('IV22')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-22",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV23 = CodeSystemConcept(
    code=f"{make_code('IV23')}",
    display="Intraoral photo,left buccal,centric relation,mirror,corrected",
    definition="Intraoral, Left Buccal Segment, Centric Relation, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-23",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.LB.CR.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV24 = CodeSystemConcept(
    code=f"{make_code('IV24')}",
    display="Intraoral photo, maxillary, mouth open, occlusal view, mirror",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-24",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV25 = CodeSystemConcept(
    code=f"{make_code('IV25')}",
    display="Intraoral photo,maxillary,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-25",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MX.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV26 = CodeSystemConcept(
    code=f"{make_code('IV26')}",
    display="Intraoral photo, mandibular, mouth open, occlusal, mirror",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-26",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MD.MO.OV.WM",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV27 = CodeSystemConcept(
    code=f"{make_code('IV27')}",
    display="Intraoral photo,mandibular,mouth open,occlusal,mirror,corrected",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-27",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.MD.MO.OV.WM.BC",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV28 = CodeSystemConcept(
    code=f"{make_code('IV28')}",
    display="Intraoral photo, showing gingival recession",
    definition="Intraoral, showing Gingival Recession (ISO tooth numbers)",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-28",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.GR.[tooth number]",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV29 = CodeSystemConcept(
    code=f"{make_code('IV29')}",
    display="Intraoral photo, showing frenum",
    definition="Intraoral, showing Frenum (ISO tooth numbers)",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-29",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.FR.[tooth number]",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)

IV30 = CodeSystemConcept(
    code=f"{make_code('IV30')}",
    display="Intraoral photo, using photo accessory",
    definition="Intraoral, any photo using a photo accessory device (modifiers)",
    designation=[
        CodeSystemConceptDesignation(
            value="IV-30",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
        CodeSystemConceptDesignation(
            value="IO.[modifier].PA",
            use={
                "system": "http://snomed.info/sct",
                "code": "900000000000013009",
                "display": "Synonym"
            }
        ),
    ]
)
