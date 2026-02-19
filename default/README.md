# Example105 Math Operations

## Overview
This project provides basic math operations (addition, subtraction) implemented in Python, with production-quality tests and CI integration.

## Usage
Import functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result = add(3, 2)  # 5
result2 = subtract(5, 3)  # 2
```

## Testing
All tests are located in the `tests` directory. Run tests using:

```
pytest tests/
```

## CI/CD Workflow
GitHub Actions workflow is defined in `.github/workflows/ci.yml`. See `default/math.json` for metadata.
