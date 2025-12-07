import pytest
from src.gooses.Goose import Goose


def test_goose_invalid_name():
    with pytest.raises(TypeError):
        Goose(123, 5)


def test_goose_invalid_volume_type():
    with pytest.raises(TypeError):
        Goose("G", "loud")


def test_goose_negative_volume():
    with pytest.raises(ValueError):
        Goose("G", -1)
