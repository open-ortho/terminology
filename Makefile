NAME = terminology
VERSION = $(shell grep -oP '(?<=version = ")[^"]*' pyproject.toml)
DIST = docs

.PHONY: clean deploy

build:
	oo-codes

dist:
	python3 -m build 

deploy: dist
	twine upload $(DIST)/*

clean:
	find $(DIST) -mindepth 1 ! -name 'CNAME' -delete
	find . -name '*.pyc' -delete
	find . -name '*.egg-info' -delete
	rm -rf *.egg-info
