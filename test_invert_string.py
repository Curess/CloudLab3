# test_invert_string.py
import pytest
from invert_string import invert  # змінено з invert_string на invert

def test_invert():
    assert invert("hello") == "olleh"  # змінено з invert_string на invert
    assert invert("Привіт") == "тівирП"  # змінено з invert_string на invert

