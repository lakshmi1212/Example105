import pytest
from src.math_operations import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (100, 200, 300),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (1e6, 1e6, 2e6),
])
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_type_error():
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')
