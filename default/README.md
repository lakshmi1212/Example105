# Example105 Math Operations

This repository implements basic math operations (addition, subtraction) and provides comprehensive tests and CI workflow integration.

## Project Structure

- `src/` - Source code for math operations
- `tests/` - Pytest test cases for all operations
- `default/requirements.txt` - Python dependencies
- `default/math.json` - CI workflow metadata

## Usage

```
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 3))   # 2
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/
```

## CI Workflow

The workflow file is located at `.github/workflows/ci.yml` and is generated based on `default/math.json` metadata.
