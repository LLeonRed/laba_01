from src.toolkit.calculator import calculator
from src.toolkit.errors import calculation_error
import pytest
# ---------- Позитивные тесты ----------

def test_addition():
    assert calculator.evaluate("12+34") == 46


def test_subtraction():
    assert calculator.evaluate("50-17") == 33


def test_multiplication():
    assert calculator.evaluate("6*7") == 42


def test_division():
    assert calculator.evaluate("20/4") == 5


def test_float_numbers():
    assert calculator.evaluate("2.5+1.5") == 4


def test_negative_number():
    assert calculator.evaluate("-5+10") == 5


def test_unary_plus():
    assert calculator.evaluate("+5+3") == 8


def test_spaces():
    assert calculator.evaluate(" 12 + 34 ") == 46


def test_operator_precedence():
    assert calculator.evaluate("2+3*4") == 14

def test_mixed_operations():
    assert calculator.evaluate("10+20*2") == 50


def test_negative_result():
    assert calculator.evaluate("5-10") == -5


def test_division_float():
    assert calculator.evaluate("5/2") == 2.5


def test_decimal_multiplication():
    assert calculator.evaluate("1.5*2") == 3


def test_unary_minus_after_operator():
    assert calculator.evaluate("10*-2") == -20


def test_multiple_operations():
    assert calculator.evaluate("10+20-5*2") == 20

# ---------- Негативные тесты ----------

def test_empty_expression():
    with pytest.raises(calculation_error):
        calculator.evaluate("")


def test_invalid_character():
    with pytest.raises(calculation_error):
        calculator.evaluate("2+a")


def test_two_operators():
    with pytest.raises(calculation_error):
        calculator.evaluate("2++*3")


def test_division_by_zero():
    with pytest.raises(calculation_error):
        calculator.evaluate("10/0")


def test_missing_operand():
    with pytest.raises(calculation_error):
        calculator.evaluate("10+")