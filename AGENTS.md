# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the top-level entry point for ad-hoc experiments.
- `html2pdf/` contains a small HTML-to-PDF workflow (`create_pdf.py`, `template.html`, `datalist.csv`, and saved output in `save/`).
- `mhxx/` and `x_mp4/` are script-focused subprojects (e.g., `mhxx/ss.py`, `x_mp4/download.py`).
- `other/` holds miscellaneous scripts and scratch code.
- `memo/` is a collection of notes and snippets (files without extensions are plain text).

## Build, Test, and Development Commands
- `python main.py` runs the top-level script.
- `python html2pdf/create_pdf.py` generates PDFs using the HTML template and CSV data.
- If you use uv for dependency management (see `uv.lock`): `uv sync` installs dev dependencies.
- Lint/format with Ruff: `ruff check .` and `ruff format .`.
- Optional type checks with Ty: `ty check .`.

## Coding Style & Naming Conventions
- Python 3.12+ is required (see `pyproject.toml`).
- Use 4-space indentation and keep functions small and task-focused.
- Scripts: `snake_case.py` file names; variables and functions in `snake_case`.
- Keep datasets and templates close to the scripts that use them (e.g., `html2pdf/`).

## Testing Guidelines
- No automated test suite is defined yet. If you add tests, place them under `tests/` and use `test_*.py` naming so common runners can discover them.

## Commit & Pull Request Guidelines
- Commit messages follow the Conventional Commits pattern (`chore: ...`, `feat: ...`, `fix: ...`).
- PRs should include a brief summary, the commands run, and sample output or screenshots when changing generated artifacts (e.g., PDFs).

## Security & Configuration Tips
- Avoid committing generated files outside intended output folders (e.g., keep PDFs under `html2pdf/save/`).
- Do not store secrets or tokens in `memo/` or scripts.

## Agent-Specific Instructions
- Respond in Japanese for all future communications.
