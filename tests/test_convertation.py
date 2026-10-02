import pytest

from src.toolkit.converter import converter


# Положительные тесты

def test_length_cm_to_m():
    assert converter.verification(100, "cm", "m") == 1


def test_length_m_to_km():
    assert converter.verification(1000, "m", "km") == 1


def test_length_km_to_mm():
    assert converter.verification(1, "km", "mm") == 1_000_000


def test_mass_kg_to_g():
    assert converter.verification(2, "kg", "g") == 2000


def test_mass_g_to_kg():
    assert converter.verification(5000, "g", "kg") == 5


def test_temperature_c_to_f():
    assert converter.verification(0, "c", "f") == 32


def test_temperature_f_to_c():
    assert converter.verification(32, "f", "c") == 0


def test_temperature_c_to_k():
    assert converter.verification(0, "c", "k") == 273.15


def test_case_insensitive_units():
    assert converter.verification(100, "CM", "M") == 1


# Негативные тесты

def test_incompatible_length_and_mass():
    with pytest.raises(Exception):
        converter.verification(100, "cm", "kg")


def test_incompatible_mass_and_temperature():
    with pytest.raises(Exception):
        converter.verification(100, "g", "c")


def test_unknown_from_unit():
    with pytest.raises(Exception):
        converter.verification(100, "abc", "m")


def test_unknown_to_unit():
    with pytest.raises(Exception):
        converter.verification(100, "cm", "abc")


def test_invalid_temperature_unit():
    with pytest.raises(Exception):
        converter.verification(100, "c", "xyz")