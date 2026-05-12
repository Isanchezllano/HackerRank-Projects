from get_the_day import find_day  # Replace 'your_module' with the actual module name

def test_find_day():
    assert find_day("08 05 2015") == "WEDNESDAY"
    assert find_day("02 29 2020") == "SATURDAY"
    assert find_day("12 25 2023") == "MONDAY"
    assert find_day("01 01 2000") == "SATURDAY"