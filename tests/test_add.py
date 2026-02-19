import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (-5, -5, -10),
    (2.5, 3.5, 6.0),
    (1e6, 1e6, 2e6)
])
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_typeerror():
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')
