import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (100, 200, 300),
    (-5, 10, 5),
    (1.5, 2.5, 4.0),
    (-1.5, 2.5, 1.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_add_type_error():
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')
    with pytest.raises(TypeError):
        add(None, 2)
