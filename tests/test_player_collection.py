from src.players.player import Player
from src.players.player_collection import PlayerCollection


def test_add_and_len():
    pc = PlayerCollection()
    pc.add(Player("A", 100))
    pc.add(Player("B", 200))
    assert len(pc) == 2


def test_slice_returns_new_collection():
    pc = PlayerCollection([
        Player("A", 10),
        Player("B", 20),
        Player("C", 30),
    ])

    sliced = pc[0:2]

    assert isinstance(sliced, PlayerCollection)
    assert len(sliced) == 2
    assert sliced[0].name == "A"
    assert sliced[1].name == "B"


def test_remove_by_name():
    pc = PlayerCollection([Player("A", 50)])
    removed = pc.remove("A")
    assert removed.name == "A"
    assert len(pc) == 0


def test_contains_by_name():
    pc = PlayerCollection([Player("A", 50)])
    assert "A" in pc
    assert "B" not in pc
