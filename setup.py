from setuptools import setup

# Read the version from the VERSION file
with open('VERSION') as version_file:
    version = version_file.read().strip()

setup(
    version=version,
)