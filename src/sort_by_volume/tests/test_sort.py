import pytest

from sort_by_volume.main import sort


# ---------- BASIC CLASSIFICATION TESTS ----------

def test_standard_package():
    assert sort(50, 50, 50, 10) == "STANDARD"


def test_heavy_package_only():
    # heavy >= 20 kg but not bulky
    assert sort(50, 50, 50, 20) == "SPECIAL"


def test_bulky_package_only_by_dimension():
    # any dimension >= 150 cm
    assert sort(150, 50, 50, 10) == "SPECIAL"


def test_bulky_package_only_by_volume():
    # volume >= 1_000_000 cm³
    assert sort(100, 100, 100, 5) == "SPECIAL"


def test_rejected_package_bulky_and_heavy():
    assert sort(100, 100, 100, 25) == "REJECTED"


# ---------- INPUT VALIDATION TESTS ----------

def test_negative_dimension_raises():
    with pytest.raises(ValueError, match="cannot be negative"):
        sort(-10, 20, 30, 5)


def test_non_numeric_input_raises():
    with pytest.raises(ValueError, match="must be a number"):
        sort("abc", 20, 30, 5)


# ---------- NUMERIC STRING INPUTS ----------

def test_numeric_string_inputs():
    assert sort("50", "50", "50", "10") == "STANDARD"
    assert sort("150", "10", "10", "10") == "SPECIAL"
    assert sort("150", "10", "10", "20") == "REJECTED"