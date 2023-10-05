# test_invert_string.py
import pytest
from invert_string import invert_string

def test_invert_string():
    assert invert_string("hello") == "olleh"
    assert invert_string("Привіт") == "тівирП"
