from fastapi import FastAPI, HTTPException
from fhir.resources.parameters import Parameters
from fhir.resources.valueset import ValueSet
import pkgutil
import importlib
import terminology.resources.value_sets as value_sets
import logging

app = FastAPI()

@app.get("/CodeSystem/$lookup")
def lookup_code(code: str, system: str):
    # Implement the logic to lookup the code in the specified code system
    # For now, return a mock response
    parameters = Parameters.construct(
        resourceType="Parameters",
        parameter=[
            {"name": "code", "valueString": code},
            {"name": "system", "valueUri": system},
            {"name": "display", "valueString": "Example Display"}
        ]
    )
    logging.info(parameters.json(indent=2))  # Log the JSON representation of the resource
    return parameters.dict()

@app.get("/ConceptMap/$translate")
def translate_code(code: str, system: str, targetsystem: str):
    # Implement the logic to translate the code from the source system to the target system
    # For now, return a mock response
    parameters = Parameters.construct(
        resourceType="Parameters",
        parameter=[
            {"name": "result", "valueBoolean": True},
            {"name": "message", "valueString": "Example translation successful"},
            {"name": "match", "part": [
                {"name": "code", "valueString": "translated-code"},
                {"name": "system", "valueUri": targetsystem},
                {"name": "display", "valueString": "Translated Display"}
            ]}
        ]
    )
    logging.info(parameters.json(indent=2))  # Log the JSON representation of the resource
    return parameters.dict()

@app.get("/ValueSet")
def get_valueset(url: str):
    # Implement the logic to return the ValueSet based on the URL
    # Do not expand the ValueSet in this endpoint
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required for GET request")
    ValueSetClass = find_valueset_by_url(url)
    valueset = ValueSetClass() if ValueSetClass else None
    if not valueset:
        raise HTTPException(status_code=404, detail=f"ValueSet with URL {url} not found")

    logging.info(valueset.json(indent=2))  # Log the JSON representation of the resource
    return valueset.dict()

@app.get("/ValueSet/$expand")
def expand_valueset(url: str):
    # Implement the logic to expand the ValueSet based on the URL
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required for GET request")
    ValueSetClass = find_valueset_by_url(url)
    valueset = ValueSetClass() if ValueSetClass else None
    if not valueset:
        raise HTTPException(status_code=404, detail=f"ValueSet with URL {url} not found")

    logging.info(valueset.json(indent=2))  # Log the JSON representation of the resource
    return valueset.dict()

@app.get("/ValueSet/{id}/$expand")
def expand_valueset_by_id(id: str):
    # Implement the logic to expand the ValueSet based on the ID
    # For now, return a mock response
    valueset = ValueSet.construct(
        resourceType="ValueSet",
        id=id,
        expansion={
            "identifier": "example-expansion-id",
            "timestamp": "2023-10-01T00:00:00Z",
            "contains": [
                {"system": "http://example.org/fhir/CodeSystem/example-system", "code": "example-code-1", "display": "Example Code 1"},
                {"system": "http://example.org/fhir/CodeSystem/example-system", "code": "example-code-2", "display": "Example Code 2"}
            ]
        }
    )
    logging.info(valueset.json(indent=2))  # Log the JSON representation of the resource
    return valueset.dict()


def find_valueset_by_url(url: str) -> ValueSet:
    """Find a ValueSet instance by its URL."""
    for _, module_name, _ in pkgutil.iter_modules(value_sets.__path__):
        module = importlib.import_module(f"terminology.resources.value_sets.{module_name}")
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, ValueSet) and hasattr(attr, 'static_url') and attr.static_url() == url:
                return attr
    return None


def expand_valueset(valueset: ValueSet) -> ValueSet:
    """Expand a ValueSet."""
    # Implement the logic to expand the ValueSet
    if valueset.compose:
        # For demonstration purposes, we will simply copy the compose element to the expansion element
        if "include" in valueset.compose:

            valueset.expansion = valueset.compose
    return valueset