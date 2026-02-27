"""Thin wrappers around fhir.resources models with flexible __init__ signatures.

These wrappers keep Pylance happy while preserving runtime validation from
fhir.resources (pydantic) by accepting keyword-only payloads.
"""

from typing import Any

from fhir.resources.codesystem import (
    CodeSystem as _CodeSystem,
    CodeSystemConcept as _CodeSystemConcept,
    CodeSystemConceptDesignation as _CodeSystemConceptDesignation,
)
from fhir.resources.conceptmap import ConceptMap as _ConceptMap
from fhir.resources.identifier import Identifier as _Identifier
from fhir.resources.namingsystem import NamingSystem as _NamingSystem
from fhir.resources.valueset import (
    ValueSet as _ValueSet,
    ValueSetExpansion as _ValueSetExpansion,
    ValueSetExpansionContains as _ValueSetExpansionContains,
)


class CodeSystem(_CodeSystem):
    def __init__(self, **data: Any):
        super().__init__(**data)


class CodeSystemConcept(_CodeSystemConcept):
    def __init__(self, **data: Any):
        super().__init__(**data)


class CodeSystemConceptDesignation(_CodeSystemConceptDesignation):
    def __init__(self, **data: Any):
        super().__init__(**data)


class ConceptMap(_ConceptMap):
    def __init__(self, **data: Any):
        super().__init__(**data)


class ValueSet(_ValueSet):
    def __init__(self, **data: Any):
        super().__init__(**data)


class ValueSetExpansion(_ValueSetExpansion):
    def __init__(self, **data: Any):
        super().__init__(**data)


class ValueSetExpansionContains(_ValueSetExpansionContains):
    def __init__(self, **data: Any):
        super().__init__(**data)


class NamingSystem(_NamingSystem):
    def __init__(self, **data: Any):
        super().__init__(**data)


class Identifier(_Identifier):
    def __init__(self, **data: Any):
        super().__init__(**data)
