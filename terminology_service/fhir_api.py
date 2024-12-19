from fastapi import FastAPI
from fhir.resources.valueset import ValueSet
from open_ortho_terminology.terminology.value_sets.dicom_scheduled_protocol import DicomScheduledProtocol

app = FastAPI()

@app.get("/ValueSet/DicomScheduledProtocol", response_model=ValueSet)
def get_dicom_scheduled_protocol():
    dsp = DicomScheduledProtocol()
    return dsp.dict()
