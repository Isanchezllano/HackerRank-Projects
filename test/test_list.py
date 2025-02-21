from io import StringIO
from list import modify_list

def test_modify_list(monkeypatch):

    user_input="12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint"

    monkeypatch.setattr("sys.stdin", StringIO(user_input))

    result= modify_list()

    assert result == [9, 5, 1]
