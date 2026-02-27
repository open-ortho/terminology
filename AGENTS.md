# AGENTS.md

Guidance for coding agents working in this repository.

## Scope

- This file applies to the entire repo rooted at `open-ortho/terminology`.
- Follow these instructions unless a user request explicitly overrides them.
- Keep changes minimal, targeted, and consistent with existing project patterns.

## Rule Sources Checked

- Cursor rules in `.cursor/rules/`: **none found**.
- Root `.cursorrules`: **none found**.
- Copilot instructions in `.github/copilot-instructions.md`: **none found**.
- Therefore, this `AGENTS.md` is the primary agent instruction file in-repo.

## Project Snapshot

- Language: Python (package in `terminology/`).
- Build backend: setuptools (`pyproject.toml`).
- Entry point CLI: `oo-codes` -> `terminology.main:main`.
- Main behavior: build FHIR `CodeSystem` and `ValueSet` JSON artifacts under `docs/fhir/`.
- Tests: `unittest`-based tests in `tests/`.
- Supported runtime per `pyproject.toml`: Python `>=3.11`.

## Setup Commands

- Create venv: `python3 -m venv .venv`
- Activate venv: `source .venv/bin/activate`
- Upgrade pip: `python3 -m pip install --upgrade pip`
- Install package (editable): `python3 -m pip install -e .`
- Optional build tooling: `python3 -m pip install build twine`

## Build Commands

- Primary build: `make build`
  - Runs `oo-codes` and writes generated JSON to `docs/fhir/`.
- Direct CLI equivalent: `oo-codes`
- Module form (if script shim unavailable): `python3 -m terminology.main`
- Build distribution artifacts: `python3 -m build`
- Makefile dist target: `make dist`
- Clean generated packaging artifacts: `make clean`

## Test Commands

- Run full test suite: `python3 -m unittest -v`
- Run specific test file: `python3 -m unittest tests.test_static_files_generator -v`
- Run specific test class: `python3 -m unittest tests.test_static_files_generator.TestMain -v`
- Run a single test (preferred exact form):
  - `python3 -m unittest tests.test_static_files_generator.TestMain.test_get_all_code_systems -v`

## Lint / Static Checks

- No dedicated linter config (`ruff`, `flake8`, `mypy`, `pylint`) is committed today.
- Minimum required quality gate for agents:
  - `python3 -m compileall terminology tests`
- Optional local linting (only if requested by user/maintainers):
  - `ruff check terminology tests`
  - `ruff format terminology tests`
- Do not introduce new lint tooling/config unless explicitly requested.

## Release / Publish Notes

- Version is defined in `pyproject.toml` under `project.version`.
- GitHub workflow `.github/workflows/python-publish.yml` publishes on tags `v*`.
- Manual publish path in `Makefile`:
  - `make dist`
  - `make deploy` (uses `twine upload docs/*` per current Makefile)

## File and Module Conventions

- Keep package code under `terminology/` and tests under `tests/`.
- `terminology/resources/code_systems/` contains large concept enumerations.
- `terminology/resources/value_sets/` composes value sets from code systems.
- Constants and UID maps live in `terminology/constants.py`.
- Avoid unnecessary file moves/renames in this repo.

## Import Style

- Prefer import grouping in this order:
  1. Python stdlib
  2. Third-party dependencies
  3. Local `terminology.*` imports
- Keep one import per line when practical; avoid wildcard imports.
- Use explicit symbols for readability (e.g., `from ... import ClassName`).
- Preserve existing module-level API import behavior in resource modules.

## Formatting Style

- Follow PEP 8 baseline and existing repository style.
- Use 4-space indentation; no tabs.
- Prefer line length around 88-100 chars; avoid extreme wrapping churn.
- Keep trailing whitespace out of edited files.
- Keep docstrings concise; add only when they clarify non-obvious intent.

## Typing Guidance

- Add type hints for new/modified function signatures when practical.
- Reuse existing typing style (`Dict[str, CodeSystem]`, `Type[Resource]`, etc.).
- Do not add heavy generic/type-complex refactors unless requested.
- Maintain runtime compatibility with current dependency versions.

## Naming Conventions

- Classes: `PascalCase` (e.g., `ScheduledProtocolValueSet`).
- Functions/variables: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.
- Domain concept constants (e.g., `EV01`, `IV3D01`) should remain stable.
- Keep URL/id strings stable unless change is explicitly required.

## FHIR Resource Patterns

- Existing pattern: resource classes subclass `fhir.resources` models directly.
- `static_url()` classmethod is used for canonical URL construction.
- Resource constructors populate full metadata payload via `super().__init__(...)`.
- CodeSystem concept lists are gathered from module globals in some modules.
- Preserve this behavior unless the user requests architectural change.

## Error Handling

- Fail with actionable errors; do not silently swallow exceptions.
- In build/generation paths, log validation or instantiation failures clearly.
- Prefer narrow exception handling over broad `except Exception` for new code.
- If broad exceptions are unavoidable, log context-rich messages.

## Testing Expectations For Changes

- For logic changes in `terminology/main.py` or resource wiring, run:
  - `python3 -m unittest -v`
- For quick verification during iteration, run the single targeted unittest first.
- If generation behavior changes, run `make build` and inspect `docs/fhir/` outputs.
- Do not rewrite large generated artifacts unless required by the requested change.

## Agent Workflow Expectations

- Before editing, inspect nearby modules for established conventions.
- Prefer surgical edits over broad cleanup.
- Keep public interfaces and canonical URLs backward compatible.
- Mention any generated files changed as side effects in your final report.
- If command/tooling assumptions are uncertain, choose the least risky path.

## Known Repository Quirks

- `README.md` is the main human documentation source.
- `Makefile build` depends on `oo-codes` availability in environment.
- Tests currently use `unittest`, not `pytest`.
- Some modules include large static concept tables; be careful with mass edits.
- `docs/` is used both for publishable static artifacts and build output.

## When Unsure

- Prefer compatibility and minimal change.
- Ask for clarification only when a decision is irreversible or ambiguous.
- Otherwise proceed with a sensible default and document what you assumed.
