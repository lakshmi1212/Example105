# Example105: Math Operations

## Overview
This repository provides basic math operations (addition and subtraction) with corresponding unit tests using pytest. It is designed for CI/CD integration with GitHub Actions.

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
  README.md
  math.json
  requirements.txt
```

## Usage

```
from src.math_operations import add, subtract

result1 = add(2, 3)        # 5
result2 = subtract(5, 2)   # 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD

See `.github/workflows/ci.yml` for workflow configuration. The pipeline runs on feature branches and main, generating HTML and JUnit test reports.
