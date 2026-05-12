from roman_number import roman_to_int

def test_roman_to_int():
    assert roman_to_int("I") == 1
    assert roman_to_int("IV") == 4
    assert roman_to_int("LX") == 60
    assert roman_to_int("XL") == 40