from app.core.calculation_factory import CalculationFactory
import pytest


def test_add():
    assert CalculationFactory.compute(2, 3, "Add") == 5


def test_sub():
    assert CalculationFactory.compute(5, 3, "Sub") == 2


def test_multiply():
    assert CalculationFactory.compute(4, 5, "Multiply") == 20


def test_divide():
    assert CalculationFactory.compute(10, 2, "Divide") == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        CalculationFactory.compute(10, 0, "Divide")


def test_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.compute(2, 3, "Power")
