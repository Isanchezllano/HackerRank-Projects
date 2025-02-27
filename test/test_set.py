from set import set_remove_discard_pop
from io import StringIO


def test_me_la_vuela_2(monkeypatch, capsys):
    inputs = """5
1 2 3 4 5
3
remove 3
discard 5
pop""".split("\n")

    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))

    set_remove_discard_pop()

    captured = capsys.readouterr()
    assert captured.out.strip() == "2"
