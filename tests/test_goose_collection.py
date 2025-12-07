from src.gooses.Goose import Goose, WarGoose, HonkGoose
from src.gooses.goose_collection import GooseCollection


def test_add_and_iter():
    gc = GooseCollection()
    gc.add(Goose("G1", 5))
    gc.add(WarGoose("G2", 10))
    assert len(list(gc)) == 2


def test_slice():
    gc = GooseCollection([
        Goose("G1", 1),
        Goose("G2", 2),
        Goose("G3", 3),
    ])

    sliced = gc[1:]
    assert isinstance(sliced, GooseCollection)
    assert len(sliced) == 2
    assert sliced[0].name == "G2"
    assert sliced[1].name == "G3"


def test_remove_by_name():
    gc = GooseCollection([Goose("G1", 5)])
    removed = gc.remove("G1")
    assert removed.name == "G1"
    assert len(gc) == 0
