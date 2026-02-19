# Example105 Math Operations

## Overview
This project implements basic math operations (addition and subtraction) with production-ready test automation and CI/CD integration.

## Usage

### Math Operations
- `src/math_operations.py` provides `add(a, b)` and `subtract(a, b)` functions.

### Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
- CI is triggered on push to `Feature1` and pull requests to `main`.
- Workflow file: `.github/workflows/ci.yml`
- Reports are generated in the `reports` folder.

## Structure
- `src/`: Source code
- `tests/`: Pytest test cases
- `default/`: Project documentation, requirements, and metadata
