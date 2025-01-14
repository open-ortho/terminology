[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/open-ortho/terminology">
    <img src="https://raw.githubusercontent.com/open-ortho/dicom4ortho/master/images/open-ortho.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">open-ortho terminology</h3>

  <p align="center">
    A collection of codes and terms from various terminologies, specifically tailored for software development within the orthodontic domain.
    <br />
    <a href="https://open-ortho.github.io/terminology/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/open-ortho/terminology">View Demo</a>
    ·
    <a href="https://github.com/open-ortho/terminology/issues">Report Bug</a>
    ·
    <a href="https://github.com/open-ortho/terminology/issues">Request Feature</a>
  </p>
</p>

## About The Project

This project serves as a centralized repository for orthodontic software developers, offering a curated collection of essential codes required for implementing healthcare standards like DICOM or HL7. Navigating through various terminologies to find the right codes can be challenging. Our project aims to simplify this process by providing a go-to source for these codes, readily available in JSON and CSV formats. Users can access these directly through GitHub releases or utilize them as a Python package on PyPI.

The primary aim of this project is to implement in FHIR Terminology the views and view sets defined in *AMERICAN NATIONAL STANDARD INSTITUTE/AMERICAN DENTAL ASSOCIATION STANDARD NO. 1100 – 2D and 3D Orthodontic/Craniofacial/Forensic Photographic Views and View Sets*. By adhering to the ADA1100 standard, we ensure that the codes and terminologies used in orthodontic software are consistent, accurate, and interoperable across different systems. This is not an official FHIR CodeSystem. The purpose for this site is to provide developers codes necessary to move forward with their development, while the codes get added and approved in official nomenclatures (like SNOMED-CT).

## Using The Codes

The codes systems and code values should be built by the Makefile and deployed in `/docs`, where github can serve them. This should serve as a static service, for CodeSystem definitions.

The codesystems are availble through the following official URLs:

- http://terminology.open-ortho.org/fhir/extraoral-2d-photographic-views
- http://terminology.open-ortho.org/fhir/intraoral-2d-photographic-views
- http://terminology.open-ortho.org/fhir/extraoral-3d-visible-light-views
- http://terminology.open-ortho.org/fhir/intraoral-3d-visible-light-views

### Python

If you want to use the codes directly in your Python project:

    pip install open-ortho-terminology

Then

    from open_ortho_terminology.terminology import hl7 as codes_hl7

    print(f"{codes_hl7.orthodontic.system}")
    print(codes_hl7.orthodontic.code)
    print(codes_hl7.orthodontic.display)

Convert codes to JSON

    from open_ortho_terminology.terminology import hl7 as codes_hl7

    print(f"{codes_hl7.orthodontic.to_json()}")

### JSON

Just point your code to any of the following:


## Releases

- Each new release must be git tagged with v*.*.*. This triggers the Github actions to publish to PyPi and release in GitHub releases.
- Version should only be stored in the `pyproject.toml` file in `project.version`, and imported accordingly when needed.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/open-ortho/terminology.svg?style=for-the-badge
[contributors-url]: https://github.com/open-ortho/terminology/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/open-ortho/terminology.svg?style=for-the-badge
[forks-url]: https://github.com/open-ortho/terminology/network/members
[stars-shield]: https://img.shields.io/github/stars/open-ortho/terminology.svg?style=for-the-badge
[stars-url]: https://github.com/open-ortho/terminology/stargazers
[issues-shield]: https://img.shields.io/github/issues/open-ortho/terminology.svg?style=for-the-badge
[issues-url]: https://github.com/open-ortho/terminology/issues
[license-shield]: https://img.shields.io/github/license/open-ortho/terminology.svg?style=for-the-badge
[license-url]: https://github.com/open-ortho/terminology/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/open-ortho
[product-screenshot]: images/screenshot.png
[example-csv-url]: resources/example/input_from.csv