NAME = terminology
VERSION = $(shell grep -oP '(?<=version = ")[^"]*' pyproject.toml)
DIST = docs

.PHONY: clean deploy

build:
	mkdir -p $(DIST)/fhir/CodeSystem
	oo-codes

dist:
	python3 -m build 

deploy: dist
	twine upload $(DIST)/*

clean:
	rm -rf build $(DIST)
	find . -name '*.pyc' -delete
	find . -name '*.egg-info' -delete
	rm -rf *.egg-info

build_docker:
	docker build -t open-ortho/terminology:$(VERSION) -t open-ortho/terminology:latest .