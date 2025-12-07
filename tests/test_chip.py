import pytest
from src.casino.chip import Chip


def test_chip_add_chip():
    c1 = Chip(10)
    c2 = Chip(5)
    result = c1 + c2
    assert isinstance(result, Chip)
    assert result.value == 15


def test_chip_add_int():
    c = Chip(7)
    result = c + 3
    assert result.value == 10


def test_int_add_chip():
    c = Chip(8)
    result = 2 + c
    assert result.value == 10


def test_chip_invalid_value():
    with pytest.raises(TypeError):
        Chip("10")

    with pytest.raises(ValueError):
        Chip(-5)


