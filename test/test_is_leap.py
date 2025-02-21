from leap_year import is_leap


def test_is_leap():
    year = 1900
    result = is_leap(year)

    assert result == False

def test_is_leap2():
    year = 2024
    result = is_leap(year)

    assert result == True
