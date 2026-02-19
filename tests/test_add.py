import pytest
from src.math_operations import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4.0),
    (-2, 3, 1),
    (1000, 1000, 2000),
    (-5, 5, 0),
])
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_type_error():
    with pytest.raises(TypeError):
        add('a', 1)
    with pytest.raises(TypeError):
        add(1, None)
