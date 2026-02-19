# Example105: Math Operations

## Overview
This repository provides basic math operations (addition, subtraction) with production-ready test automation using pytest and a CI workflow.

## Structure
- `src/`: Source code for math operations
- `tests/`: Pytest test cases for each operation
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI/CD metadata for workflow generation

## Usage
```python
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests
Install dependencies:
```bash
pip install -r default/requirements.txt
```
Run all tests:
```bash
pytest tests/
```

## CI Workflow
The repository is set up for GitHub Actions CI using the metadata in `default/math.json`.
