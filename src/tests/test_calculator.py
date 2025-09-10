"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator
import pytest


@pytest.fixture
def calculator():
    yield Calculator()

def test_app():
    my_calculator = Calculator()
    #assert my_calculator.get_hello_message() == "Calculatrice"
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition(calculator):
    assert calculator.addition(2, 3) == 5


def test_subtraction(calculator):
    assert calculator.subtraction(10, 7) == 3

def test_multiplication(calculator):
    assert calculator.multiplication(5, 7) == 35
    assert calculator.multiplication(-5, 7) == -35
    assert calculator.multiplication(-5, -7) == 35
    assert calculator.multiplication(5, -7) == -35
    assert calculator.multiplication(9, 0) == 0
    assert calculator.multiplication(0, 9) == 0


def test_division(calculator):
    assert calculator.division(10, 5) == 2
    assert calculator.division(10, 0) == "Erreur : division par zéro"

# TODO: ajoutez les tests

def test_ad(calculator):
    calculator.addition(2,5) == 7