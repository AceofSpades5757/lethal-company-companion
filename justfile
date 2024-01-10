set shell := ["nu", "-c"]

PYTHON_VERSION := "3.12"
PYTHON := if os_family() == "windows" { "py" } else { "python3" }
VENV_DIR := ".venv"
VENV_BIN := VENV_DIR / if os_family() == "windows" { "Scripts" } else { "bin" }
VENV_PYTHON := VENV_BIN / "python.exe"

help:
	@just --list

venv:
    if not ("{{VENV_DIR}}" | path exists) { just _venv; }

_venv:
    {{PYTHON}} -m pip install --upgrade pip
    {{PYTHON}} -m pip install --upgrade virtualenv
    {{PYTHON}} -m virtualenv --python {{PYTHON_VERSION}} {{VENV_DIR}}
    {{VENV_PYTHON}} -m pip install --upgrade pip
    {{VENV_PYTHON}} -m pip install -e .[dev]

mostlyclean:
    # Cache Files
    fd --glob "*.egg-info" --no-ignore --exec rm -r
    fd --glob "__pycache__" --no-ignore --exec rm -r

clean: mostlyclean
    # Virtual Environment
    rm -rf "{{VENV_DIR}}"

format: venv
	{{VENV_BIN}}/pre-commit run --all-files

format-update: venv
	{{VENV_BIN}}/pre-commit autoupdate

type: venv
	{{VENV_BIN}}/mypy ./src
