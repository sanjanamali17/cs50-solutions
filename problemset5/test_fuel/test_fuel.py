import pytest
from fuel import convert, gauge


def test_convert_basic():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_edges():
    assert convert("0/100") == 0
    assert convert("100/100") == 100


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
