import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (0, 0, 0),
    (-1, 1, -2),
    (200, 100, 100),
    (-5, -5, 0),
    (7.5, 2.5, 5.0),
    (1e6, 1e5, 9e5)
])
def test_subtract_basic(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_typeerror():
    with pytest.raises(TypeError):
        subtract('a', 2)
    with pytest.raises(TypeError):
        subtract(1, 'b')
