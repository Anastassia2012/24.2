import pytest
from app.calc import Calculator



def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(4, 5)
    assert result == 20

def test_division():
    calculator = Calculator()
    result = calculator.division(10, 2)
    assert result == 5

def test_subtraction():
    calculator = Calculator()
    result = calculator.subtraction(7, 3)
    assert result == 4

def test_adding():
    calculator = Calculator()
    result = calculator.adding(6, 9)
    assert result == 15
