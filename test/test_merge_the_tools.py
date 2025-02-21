from merge_the_tools import merge_the_tools

def test_merge_the_tools():

    result = merge_the_tools("AABCAAADA", 3)
    assert result == "AB CA AD"