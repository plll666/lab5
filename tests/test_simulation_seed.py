from src.casino.casino import Casino
from src.players.player import Player
from src.gooses.Goose import Goose


def test_simulation_is_deterministic_with_seed():
    c1 = Casino()
    c2 = Casino()

    c1.register_player(Player("A", 100))
    c2.register_player(Player("A", 100))

    c1.register_goose(Goose("G1", 5))
    c2.register_goose(Goose("G1", 5))

    c1.run_simulation(steps=10, seed=123)
    c2.run_simulation(steps=10, seed=123)

    assert c1.balances["A"] == c2.balances["A"]
