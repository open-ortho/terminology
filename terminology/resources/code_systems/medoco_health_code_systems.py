from fhir.resources.codesystem import CodeSystem, CodeSystemConcept
from datetime import datetime, timezone
from terminology.resources.naming_systems import MedocoHealthNamingSystem


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


class OrthodonticPhotographViewsCodeSystem(CodeSystem):

    @classmethod
    def static_url(cls) -> str:
        ns = MedocoHealthNamingSystem()
        return f"{ns.url}/{ns.name}/CodeSystem/OrthodonticPhotographViews"

    def __init__(self):
        MDOC = MedocoHealthNamingSystem()
        super().__init__(
            url=self.static_url(),
            version="1.0.0",
            name=MDOC.name,
            title="medoco Health Orthodontic Photographic Views Code System",
            status="draft",
            experimental=True,
            date=datetime.now().date().isoformat(),
            publisher="medoco Health",
            description=MDOC.description,
            caseSensitive=True,
            content="complete",
            concept=[value for name, value in globals().items() if isinstance(value, CodeSystemConcept)]
        )



EV07 = CodeSystemConcept(
    code=f"{make_code('EV07')}",
    display="EV-07 EO.RP.MD.PF",
    definition="Extraoral, Right Profile (subject is facing observer's right), Mandible Postured Forward",
)
