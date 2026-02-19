# Example105: Math Operations

## Overview
This repository provides basic math operations (`add` and `subtract`) in Python, with comprehensive tests and a ready-to-use CI workflow.

## Structure
- `src/`: Source code for math operations
- `tests/`: Pytest-based test cases
- `default/requirements.txt`: Project dependencies
- `default/math.json`: Metadata for workflow automation

## Usage

### Math Operations
```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
```

### Running Tests
Install requirements and run:
```
pip install -r default/requirements.txt
pytest tests/
```

### CI/CD
The repository is ready for GitHub Actions CI using the workflow defined in `.github/workflows/ci.yml` (see `default/math.json` for workflow metadata).

## Requirements
- Python 3.10+
- pytest
- pytest-html

## Contributing
Please submit PRs to the `Feature1` branch.
