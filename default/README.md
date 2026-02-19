# Example105: Math Operations

## Overview
This project provides basic math operations (addition and subtraction) and corresponding pytest-based tests. CI workflow is defined for automated testing.

## Usage

- Import from `src.math_operations`:

```python
from src.math_operations import add, subtract
print(add(1, 2))
print(subtract(3, 1))
```

## Testing

Run tests with:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow

- CI is configured via `.github/workflows/ci.yml`.
- Test reports are generated in `reports/`.

## Structure

- `src/`: Business logic
- `tests/`: Test cases
- `default/`: Metadata, requirements, README
