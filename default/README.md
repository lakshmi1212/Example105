# Example105: Math Operations

This repository provides simple math operations (addition and subtraction) and corresponding automated tests using pytest.

## Structure

- `src/`: Source code for math operations
- `tests/`: Pytest-based unit tests
- `default/`: Project metadata and requirements

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/
   ```

## CI/CD Workflow
- Workflow file: `.github/workflows/ci.yml`
- Runs on: push to `Feature1` and pull request to `main`
- Generates HTML and JUnit test reports in `reports/`

## Python Version
- Python 3.10
