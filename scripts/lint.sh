#!/bin/bash
set -e

echo "--- Running Ruff (Linter) ---"
uv run ruff check .

echo "--- Running Mypy (Type Check) ---"
uv run mypy .

echo "All checks passed!"
