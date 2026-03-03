import pytest
from coffeecup import calculate_total, apply_discount

def test_calculate_total():
    assert calculate_total("espresso", 2) == 200

def test_invalid_coffee():
    with pytest.raises(ValueError):
        calculate_total("mocha", 1)

def test_invalid_quantity():
    with pytest.raises(ValueError):
        calculate_total("latte", 0)

def test_apply_discount():
    assert apply_discount(200, 10) == 180

def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(200, 120)