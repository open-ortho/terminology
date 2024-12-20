from fastapi import FastAPI
from fhir.resources.valueset import ValueSet
from terminology.resources.value_sets.dicom_scheduled_protocol import DicomScheduledProtocol
import logging

app = FastAPI()

@app.get("/ValueSet/DicomScheduledProtocol")
def get_dicom_scheduled_protocol():
    dsp = DicomScheduledProtocol()
    logging.info(dsp.json(indent=2))  # Log the JSON representation of the resource
    return dsp.dict()
