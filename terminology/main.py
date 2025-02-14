#!/usr/bin/env python3
""" Convert Python code modules to JSON and CSV for publication.

When adding new modules:

- Import module
- Add new module to for loop in __main__
"""
import sys
import json
import types
from pathlib import Path
from typing import Any, Type, Dict
import uuid
import inspect
from datetime import datetime

from fhir.resources.resource import Resource
from fhir.resources.codesystem import CodeSystem
from fhir.resources.valueset import ValueSet
from pydantic import ValidationError

from terminology.resources.code_systems import (
    dentaleyepad_image_types,
    extraoral_2d_photographic_scheduled_protocol,
    extraoral_3d_visible_light_scheduled_protocol,
    intraoral_3d_visible_light_scheduled_protocol,
    intraoral_2d_photographic_scheduled_protocol,
    ada_1100_enumerated_terms
)

from terminology.resources.value_sets import (
    scheduled_protocol
)

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)


build_path = Path('.', 'docs')

all_code_systems = None

def expand_valueset(valueset: ValueSet, all_code_systems: Dict[str, CodeSystem]) -> Dict:
    """Expand a ValueSet by including all codes from referenced CodeSystems.
    
    Args:
        valueset: ValueSet instance to expand
        all_code_systems: Dictionary of all available CodeSystem resources
        
    Returns:
        Dict containing the expanded ValueSet with all codes included
    """
    expanded = valueset.model_dump()
    
    # Add expansion section
    expanded["expansion"] = {
        "identifier": f"urn:uuid:{uuid.uuid4()}",
        "timestamp": datetime.now().isoformat(),
        "total": 0,
        "contains": []
    }
    
    # Process each included system
    for include in valueset.compose.include:
        system_url = include.system
        if not system_url:
            continue
            
        # Find the referenced CodeSystem instance
        cs_instance = all_code_systems.get(system_url)
        
        if cs_instance:
            # Add all concepts from this CodeSystem
            for concept in cs_instance.concept:
                expanded["expansion"]["contains"].append({
                    "system": system_url,
                    "code": concept.code,
                    "display": concept.display
                })
        else:
            logger.warning(f"CodeSystem with URL {system_url} not found.")
                
    # Update total count
    expanded["expansion"]["total"] = len(expanded["expansion"]["contains"])
    return expanded

def save_fhir_resource(module: Any, resource_type: Type[Resource], filename: Path) -> None:
    """Save any FHIR resource to JSON file.
    
    Args:
        module: Python module containing FHIR resource classes
        resource_type: Type of FHIR resource to look for (CodeSystem, ValueSet, etc)
        filename: Base path where to save the JSON files
    """
    logger.info(f"Processing {module.__name__} for {resource_type.__name__}")

    resources = {
        name: getattr(module, name) for name in dir(module)
        if isinstance(getattr(module, name), type) 
        and issubclass(getattr(module, name), resource_type)
    }

    if not resources:
        logger.warning(
            f"No {resource_type.__name__} instances found in module {module.__name__}")
        return

    for name, resource_class in resources.items():
        try:
            resource_instance = resource_class()
            
            # Generate base filename from resource URL
            base_filename = filename / resource_instance.url.split('/')[-1]
            base_filename.parent.mkdir(parents=True, exist_ok=True)
            
            # Save the basic resource
            logger.info(f"Saving {resource_class.__name__} to {base_filename}")
            with open(base_filename, 'w') as f:
                json.dump(resource_instance.model_dump(), f, indent=4)
            
            # If it's a ValueSet, also save expanded version
            if isinstance(resource_instance, ValueSet):
                expanded_filename = filename / f"{resource_instance.url.split('/')[-1]}-expanded"
                logger.info(f"Saving expanded {resource_class.__name__} to {expanded_filename}")
                
                expanded = expand_valueset(resource_instance, all_code_systems)
                with open(expanded_filename, 'w') as f:
                    json.dump(expanded, f, indent=4)
                    
        except ValidationError as e:
            logger.debug(f"{resource_type.__name__} {resource_class.__name__} is not valid")
            continue

def get_all_code_systems() -> Dict[str, CodeSystem]:
    """Collect all CodeSystem instances from the available modules.
    
    Returns:
        Dictionary of all available CodeSystem instances
    """
    global all_code_systems
    if all_code_systems:
        return all_code_systems

    from terminology.resources import code_systems
    all_code_systems = {}
    for name in dir(code_systems):
        obj = getattr(code_systems, name)
        if isinstance(obj, types.ModuleType):
            for subname in dir(obj):
                subobj = getattr(obj, subname)
                if isinstance(subobj, type) and issubclass(subobj, CodeSystem) and subobj != CodeSystem:
                    try:
                        instance = subobj()
                        all_code_systems[instance.url] = instance
                    except Exception as e:
                        logger.warning(f"Could not instantiate {subobj.__name__}: {e}")
    return all_code_systems

def main():
    global all_code_systems
    all_code_systems = get_all_code_systems()
    # Dictionary mapping resource types to modules containing them
    resources = {
        # CodeSystem: [
        #     extraoral_2d_photographic_scheduled_protocol,
        #     extraoral_3d_visible_light_scheduled_protocol,
        #     intraoral_3d_visible_light_scheduled_protocol,
        #     intraoral_2d_photographic_scheduled_protocol,
        #     dentaleyepad_image_types,
        #     ada_1100_enumerated_terms
        # ],
        ValueSet: [
            scheduled_protocol
        ]
    }

    # Process each resource type and its modules
    for resource_type, modules in resources.items():
        for module in modules:
            save_fhir_resource(module, resource_type, build_path / 'fhir')

if __name__ == "__main__":
    sys.exit(main())
