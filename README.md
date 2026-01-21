# python_core_vivin

core code base for all my python related work

## Overview

This repository contains a minimal, reusable Python package layout to serve as the core for Python projects. It uses the "src/" layout, includes a small example function, and a unit test so you can verify the project is working immediately.

## What I added

- src/python_core_vivin/: package source
- tests/: unittest-based tests (runs with the built-in test runner)
- pyproject.toml: minimal build metadata
- requirements.txt: runtime/development dependencies placeholder
- .gitignore: common Python ignores

## Quickstart

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. (Optional) Install dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

3. Run the unit tests (uses built-in unittest, no extra packages required):

```powershell
python -m unittest discover -v
```

## Project structure

- src/python_core_vivin/: package code
- tests/: unit tests
- README.md
- pyproject.toml
- requirements.txt
- .gitignore


## Next steps

- Add more modules under `src/python_core_vivin/`.
- Add CI (GitHub Actions) and tooling (linters, formatters) as needed.
