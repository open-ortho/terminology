NAME = terminology
VERSION = $(shell grep -oP '(?<=version = ")[^"]*' pyproject.toml)

.PHONY: clean deploy

build:
	mkdir -p build
	python3 -m $(NAME).main

dist:
	python3 -m build 

deploy: dist
	twine upload dist/*

clean:
	rm -rf build dist
	find . -name '*.pyc' -delete
	find . -name '*.egg-info' -delete
	rm -rf *.egg-info

build_docker:
	docker build -t open-ortho/terminology:$(VERSION) -t open-ortho/terminology:latest .