#!/usr/bin/env python3
""" Convert Python code modules to JSON and CSV for publication.

When adding new modules:

- Import module
- Add new module to for loop in __main__
"""
import sys
import json
import csv
from pathlib import Path

from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.codesystem import CodeSystem
from pydantic import ValidationError

from terminology.resources import hl7, open_ortho, snomed, dentaleyepad, vendors
from terminology.resources import Code
from terminology.resources.code_systems import open_ortho_code_system, snomed_code_system, medoco_health_code_systems

import logging
logger = logging.getLogger(__name__)

build_path = Path('.', 'docs')


def save_to_fhir(module, filename):
    codes = {name: getattr(module, name) for name in dir(module)
             if isinstance(getattr(module, name), Code)}

    data = None
    if codes:
        b = Bundle(type='collection')
        b.entry = []
        for name, code in codes.items():
            be = BundleEntry()
            be.resource = code.to_fhir()
            b.entry.append(be)

        data = b.model_dump()

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def save_code_system_to_fhir(module, filename: Path):
    code_systems = {name: getattr(module, name) for name in dir(module)
                    if isinstance(getattr(module, name), type) and issubclass(getattr(module, name), CodeSystem)}

    if not code_systems:
        logger.warning("No CodeSystem instances found in the module")
        return

    for name, code_system_class in code_systems.items():
        try:
            code_system_instance = code_system_class()
        except ValidationError as e:
            logger.warning(f"CodeSystem {code_system_class.__name__} is not valid")
            continue
        print(f"Saving {code_system_class.__name__} to FHIR")
        filename = filename / code_system_instance.url.split('/')[-1]
        with open(filename, 'w') as f:
            json.dump(code_system_instance.model_dump(), f, indent=4)




def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Key', 'System', 'Code', 'Display'])
        for key, value in data.items():
            writer.writerow(
                [key, value['system'], value['code'], value['display']])


def module_to_dict(module):
    """ Convert module to dict.

    Handles both Code modules and fhir.resource.coding.Coding modules.
    """
    Codes = {name: getattr(module, name) for name in dir(module)
             if isinstance(getattr(module, name), Code)}

    if Codes:
        # Convert Code instances to dictionaries for JSON and CSV
        return {
            name: {
                'system': code.system,
                'code': code.code,
                'full_code': code.full_code,
                'display': code.display,
                'synonyms': code.synonyms,
                'contexts': code.contexts
            } for name, code in Codes.items()}


def main():
    for codes_system in (open_ortho_code_system,):
        save_code_system_to_fhir(
            codes_system, build_path / 'fhir' )

    # for module in (snomed, hl7, vendors, open_ortho, dentaleyepad):
    #     dict_module = module_to_dict(module)
    #     save_to_fhir(module, build_path / f'{module.__name__}_fhir.json')
    #     save_to_json(dict_module, build_path / f'{module.__name__}.json')
    #     try:
    #         save_to_csv(dict_module, build_path / f'{module.__name__}.csv')
    #     except Exception as e:
    #         # logger.exception(e)
    #         logger.warning(
    #             f"Error while trying to save {module.__name__} to CSV.")


if __name__ == "__main__":
    sys.exit(main())
