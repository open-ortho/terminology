from setuptools import setup, find_packages

# Read the version from the VERSION file
with open('VERSION') as version_file:
    version = version_file.read().strip()

setup(
    version=version,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
)