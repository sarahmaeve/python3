"""Test a simple leapyear function. Demonstrate pytest."""
from leapyear import is_leapyear

def test_is_leapyear():
    """My year selections. Pylint recommended use of statement and not statement
    instead of == True or == False"""
    assert is_leapyear(2020), "value was False, should be True"
    assert not is_leapyear(2019), "value was True, should be False"
    assert not is_leapyear(1900), "value was True, should be False"
    assert is_leapyear(1600), "value was False, should be True"
    assert not is_leapyear(2010), "value was True, should be False"
