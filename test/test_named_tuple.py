from named_tuple import get_mark_student_average
from io import StringIO
from unittest.mock import patch


def test_get_mark_student_average():
    user_input = """5
    ID MARKS NAME CLASS
    1 97 Raymond 7
    2 50 Steven 4
    3 91 Adrian 9
    4 72 Stewart 5
    5 80 Peter 6"""

    with patch("sys.stdin", StringIO(user_input)), patch("sys.stdout", new_callable=StringIO) as mock_output:
        get_mark_student_average()

        assert mock_output.getvalue() == "78.0\n"
