NAME = terminology
VERSION = $(shell grep -oP '(?<=version = ")[^"]*' pyproject.toml)
DIST = docs

.PHONY: clean deploy serve help

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  build    Build FHIR artifacts into docs/ (runs oo-codes)"
	@echo "  serve    Serve docs/ on http://localhost:8000 (simulates GitHub Pages)"
	@echo "  dist     Build Python distribution packages"
	@echo "  deploy   Build dist and upload to PyPI with twine"
	@echo "  clean    Remove generated files from docs/ (preserves CNAME) and .pyc/.egg-info"
	@echo "  help     Show this help message"

build:
	oo-codes

serve:
	@echo "Serving docs/ at http://localhost:8000 (simulates GitHub Pages)"
	@echo "Press Ctrl+C to stop."
	python3 -m http.server 8000 --directory docs

dist:
	python3 -m build 

deploy: dist
	twine upload $(DIST)/*

clean:
	find $(DIST) -mindepth 1 ! -name 'CNAME' -delete
	find . -name '*.pyc' -delete
	find . -name '*.egg-info' -delete
	rm -rf *.egg-info
