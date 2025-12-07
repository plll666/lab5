from src.casino.casino_balance import CasinoBalance


def test_add_and_get():
    cb = CasinoBalance()
    cb["P1"] = 100
    assert cb["P1"] == 100


def test_update_balance():
    cb = CasinoBalance()
    cb["P1"] = 50
    cb["P1"] = 70
    assert cb["P1"] == 70


def test_contains():
    cb = CasinoBalance()
    cb["A"] = 15
    assert "A" in cb
    assert "B" not in cb


def test_total_balance():
    cb = CasinoBalance()
    cb["A"] = 10
    cb["B"] = 20
    assert cb.total_balance() == 30
