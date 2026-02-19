# math_operations.py

def add(a, b):
    """
    Add two numbers.
    Args:
        a (int|float): First number.
        b (int|float): Second number.
    Returns:
        int|float: Sum of a and b.
    Raises:
        TypeError: If inputs are not int or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    Args:
        a (int|float): First number.
        b (int|float): Second number.
    Returns:
        int|float: Result of a - b.
    Raises:
        TypeError: If inputs are not int or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a - b
