from fhir.resources.codesystem import CodeSystem, CodeSystemConcept
from fhir.resources.coding import Coding
from datetime import datetime
from typing import List
from open_ortho_terminology.terminology.naming_systems import OpenOrthoNamingSystem


def make_code(s):
    """
    Convert a string of ASCII characters to a single string of their equivalent integer values concatenated together.

    Args:
    s (str): A string to convert.

    Returns:
    str: A string consisting of the ASCII integer values concatenated together without any spaces.
    """
    # Convert each character to its ASCII integer, then to a string, and concatenate
    return ''.join(str(ord(char)) for char in s)


class OpenOrthoCodeSystem(CodeSystem):

    OPOR = OpenOrthoNamingSystem()

    def __init__(self):
        super().__init__()
        self.url = "http://open-ortho.org/terminology/fhir/CodeSystem"
        self.version = "1.0.0"
        self.name = self.OPOR.name
        self.title = "Open-Ortho Code System"
        self.status = "draft"
        self.experimental = True
        self.date = datetime.now().isoformat()
        self.publisher = "Open Ortho"
        self.description = self.OPOR.description
        self.caseSensitive = True
        self.content = "complete"

        self.concept = [EV07]


EV07 = CodeSystemConcept(
    code=f"{make_code('EV07')}",
    display="EV-07 EO.RP.MD.PF",
    definition="Extraoral, Right Profile (subject is facing observer's right), Mandible Postured Forward",
)

EV28 = CodeSystemConcept(
    code=f"{make_code('EV28')}",
    display="EV-28 EO.LP.MD.PF",
    definition="Extraoral, Left Profile (subject is facing observer's left), Mandible Postured Forward",
)

EV37 = CodeSystemConcept(
    code=f"{make_code('EV37')}",
    display="EV-37 EO.OF.SV",
    definition="Extraoral, Other Face (viewed from above), Superior View (showing forehead, infraorbital rim contour, dorsum of nose, upper lip, chin)",
)

EV38 = CodeSystemConcept(
    code=f"{make_code('EV38')}",
    display="EV-38 EO.OF.CS",
    definition="Extraoral, Other Face, Close-Up Smile (with lips)",
)

EV39 = CodeSystemConcept(
    code=f"{make_code('EV39')}",
    display="EV-39 EO.OF.OC",
    definition="Extraoral, Other Face, Occlusal Cant (e.g., tongue depressor between the teeth)",
)

EV40 = CodeSystemConcept(
    code=f"{make_code('EV40')}",
    display="EV-40 EO.OF.FI",
    definition="Extraoral, Other Face, Forensic Interest (tattoos, jewelry, scars)",
)

EV41 = CodeSystemConcept(
    code=f"{make_code('EV41')}",
    display="EV-41 EO.OF.AN",
    definition="Extraoral, Other Face, Anomalies (ears, skin tags, etc.)",
)

EV42 = CodeSystemConcept(
    code=f"{make_code('EV42')}",
    display="EV-42 EO.FF.MO",
    definition="Extraoral, Full Face, Mouth Open",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "EV-42"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "EO.FF.MO"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

EV43 = CodeSystemConcept(
    code=f"{make_code('EV43')}",
    display="EV-43 EO.FF.NW",
    definition="Extraoral, Full Face, demonstrating Nerve Weakness",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "EV-43"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "EO.FF.NW"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV01 = CodeSystemConcept(
    code=f"{make_code('IV01')}",
    display="IV-01 IO.RB.CO",
    definition="Intraoral Right Buccal Segment, Centric Occlusion, Direct View",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-01"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.RB.CO"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "DEYE-brr"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV02 = CodeSystemConcept(
    code=f"{make_code('IV02')}",
    display="IV-02 IO.RB.CO.WM",
    definition="Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-02"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.RB.CO.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV03 = CodeSystemConcept(
    code=f"{make_code('IV03')}",
    display="IV-03 IO.RB.CO.WM.BC",
    definition="Intraoral, Right Buccal Segment, Centric Occlusion, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-03"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.RB.CO.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV04 = CodeSystemConcept(
    code=f"{make_code('IV04')}",
    display="IV-04 IO.LB.CO",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, Direct View",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-04"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.LB.CO"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV05 = CodeSystemConcept(
    code=f"{make_code('IV05')}",
    display="IV-05 IO.LB.CO.WM",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-05"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.LB.CO.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV06 = CodeSystemConcept(
    code=f"{make_code('IV06')}",
    display="IV-06 IO.LB.CO.WM.BC",
    definition="Intraoral, Left Buccal Segment, Centric Occlusion, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-06"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.LB.CO.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV07 = CodeSystemConcept(
    code=f"{make_code('IV07')}",
    display="IV-07 IO.AO",
    definition="Intraoral, Anterior Occlusal, Direct View",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-07"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.AO"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV08 = CodeSystemConcept(
    code=f"{make_code('IV08')}",
    display="IV-08 IO.AO.WM",
    definition="Intraoral, Anterior Occlusal, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-08"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.AO.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV09 = CodeSystemConcept(
    code=f"{make_code('IV09')}",
    display="IV-09 IO.AO.WM.BC",
    definition="Intraoral, Anterior Occlusal, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-09"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.AO.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV10 = CodeSystemConcept(
    code=f"{make_code('IV10')}",
    display="IV-10 IO.MD.MO.OV",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-10"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MD.MO.OV"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV11 = CodeSystemConcept(
    code=f"{make_code('IV11')}",
    display="IV-11 IO.MD.MO.OV.WM",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-11"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MD.MO.OV.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV12 = CodeSystemConcept(
    code=f"{make_code('IV12')}",
    display="IV-12 IO.MD.MO.OV.WM.BC",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-12"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MD.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV13 = CodeSystemConcept(
    code=f"{make_code('IV13')}",
    display="IV-13 IO.MX.MO.OV",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-13"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV14 = CodeSystemConcept(
    code=f"{make_code('IV14')}",
    display="IV-14 IO.MX.MO.OV.WM",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-14"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV15 = CodeSystemConcept(
    code=f"{make_code('IV15')}",
    display="IV-15 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-15"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV16 = CodeSystemConcept(
    code=f"{make_code('IV16')}",
    display="IV-16 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-16"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV17 = CodeSystemConcept(
    code=f"{make_code('IV17')}",
    display="IV-17 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-17"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV18 = CodeSystemConcept(
    code=f"{make_code('IV18')}",
    display="IV-18 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-18"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV19 = CodeSystemConcept(
    code=f"{make_code('IV19')}",
    display="IV-19 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-19"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV20 = CodeSystemConcept(
    code=f"{make_code('IV20')}",
    display="IV-20 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-20"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV21 = CodeSystemConcept(
    code=f"{make_code('IV21')}",
    display="IV-21 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-21"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV22 = CodeSystemConcept(
    code=f"{make_code('IV22')}",
    display="IV-22 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-22"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV23 = CodeSystemConcept(
    code=f"{make_code('IV23')}",
    display="IV-23 IO.LB.CR.WM.BC",
    definition="Intraoral, Left Buccal Segment, Centric Relation, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-23"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.LB.CR.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV24 = CodeSystemConcept(
    code=f"{make_code('IV24')}",
    display="IV-24 IO.MX.MO.OV.WM",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-24"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV25 = CodeSystemConcept(
    code=f"{make_code('IV25')}",
    display="IV-25 IO.MX.MO.OV.WM.BC",
    definition="Intraoral, Maxillary, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-25"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MX.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV26 = CodeSystemConcept(
    code=f"{make_code('IV26')}",
    display="IV-26 IO.MD.MO.OV.WM",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-26"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MD.MO.OV.WM"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV27 = CodeSystemConcept(
    code=f"{make_code('IV27')}",
    display="IV-27 IO.MD.MO.OV.WM.BC",
    definition="Intraoral, Mandibular, Mouth Open, Occlusal View, With Mirror, But Corrected",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-27"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.MD.MO.OV.WM.BC"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV28 = CodeSystemConcept(
    code=f"{make_code('IV28')}",
    display="IV-28 IO.GR.[tooth number]",
    definition="Intraoral, showing Gingival Recession (ISO tooth numbers)",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-28"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.GR.[tooth number]"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV29 = CodeSystemConcept(
    code=f"{make_code('IV29')}",
    display="IV-29 IO.FR.[tooth number]",
    definition="Intraoral, showing Frenum (ISO tooth numbers)",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-29"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.FR.[tooth number]"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)

IV30 = CodeSystemConcept(
    code=f"{make_code('IV30')}",
    display="IV-30 IO.[modifier].PA",
    definition="Intraoral, any photo using a photo accessory device (modifiers)",
    designation=[
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IV-30"},
        {"use": Coding(system="http://open-ortho.org/fhir/CodeSystem/term-designation-use", code="synonym"), "value": "IO.[modifier].PA"}
    ],
    property=[
        {"code": "context", "valueString": "DICOM.ScheduledProtocol"}
    ]
)
