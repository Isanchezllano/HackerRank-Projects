from capitalize import solve

def test_solve():

    assert solve("   hello  world   ") == "   Hello  World   "

    assert solve("o'nel") == "O'nel"

    assert solve("Isabella sanchez lLano") == "Isabella Sanchez LLano"


