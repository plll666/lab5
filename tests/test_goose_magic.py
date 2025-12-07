from src.gooses.Goose import Goose, WarGoose


def test_goose_add_same_type():
    g1 = Goose("A", 3)
    g2 = Goose("B", 4)

    combined = g1 + g2

    assert isinstance(combined, Goose)
    assert combined.honk_volume == 7
    assert combined.name == "A&B"


def test_goose_add_different_types():
    g1 = Goose("A", 3)
    g2 = WarGoose("B", 4)

    combined = g1 + g2

    assert isinstance(combined, Goose)
    assert combined.honk_volume == 7


