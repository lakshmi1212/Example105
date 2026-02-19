def add(a, b):
    """Return the sum of two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Both arguments must be int or float')
    return a + b


def subtract(a, b):
    """Return the difference of two numbers (a - b)."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Both arguments must be int or float')
    return a - b
