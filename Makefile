NAME = terminology
VERSION = $(shell grep -oP '(?<=version = ")[^"]*' pyproject.toml)
DIST = docs

.PHONY: clean deploy serve help tests

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

build: tests
	oo-codes

serve:
	@echo "Serving docs/ at http://localhost:8000 (simulates GitHub Pages)"
	@echo "Press Ctrl+C to stop."
	python3 -m http.server 8000 --bind 127.0.0.1 --directory docs

dist: tests
	python3 -m build 

deploy: dist
	twine upload $(DIST)/*

clean:
	find $(DIST) -mindepth 1 ! -name 'CNAME' -delete
	find . -name '*.pyc' -delete
	rm -rf *.egg-info
	find . -name '*.egg-info' -delete

tests:
	python3 -m pytest tests/ -v