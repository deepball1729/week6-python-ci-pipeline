"""Unit tests for calculator operations."""

import pytest

from calculator import add, divide, multiply, subtract


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_add_negative_number() -> None:
    assert add(-2, 3) == 1


def test_subtract_numbers() -> None:
    assert subtract(9, 4) == 5


def test_multiply_numbers() -> None:
    assert multiply(3, 4) == 12


def test_multiply_by_zero() -> None:
    assert multiply(7, 0) == 0


def test_divide_numbers() -> None:
    assert divide(8, 2) == 4


def test_divide_returns_fraction() -> None:
    assert divide(5, 2) == 2.5


def test_divide_by_zero_raises_error() -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)
