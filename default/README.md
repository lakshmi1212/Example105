# Example105: Math Operations

This repository provides basic math operations (addition and subtraction) with full pytest-based test coverage and CI workflow integration.

## Project Structure

```
src/
  math_operations.py
  __init__.py

tests/
  test_add.py
  test_subtract.py
  __init__.py

default/
  requirements.txt
  README.md
  math.json
```

## Usage

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/
```

## CI/CD

The repository is designed for GitHub Actions CI/CD using the workflow in `.github/workflows/ci.yml` (to be generated from `default/math.json`).

## Math Operations

- `add(a, b)`: Returns the sum of `a` and `b`.
- `subtract(a, b)`: Returns the result of `a - b`.

## Test Coverage

- `tests/test_add.py`: Tests for addition.
- `tests/test_subtract.py`: Tests for subtraction.

## Requirements

- Python 3.10+
- pytest
- pytest-html
