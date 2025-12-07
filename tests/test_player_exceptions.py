import pytest
from src.players.player import Player


def test_player_invalid_name():
    with pytest.raises(TypeError):
        Player(123, 10)


def test_player_invalid_balance_type():
    with pytest.raises(TypeError):
        Player("A", "money")


def test_player_negative_balance():
    with pytest.raises(ValueError):
        Player("A", -5)
