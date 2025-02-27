from exceptions import practice_exceptions
from io import StringIO


def test_practice_exceptions(monkeypatch, capsys):
    inputs = """3
1 0
2 $
3 1""".split("\n")

    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))

    practice_exceptions()

    captured = capsys.readouterr()
    expected_output = """Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3"""

    assert captured.out.strip() == expected_output.strip()
