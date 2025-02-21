from students import get_second
from io import StringIO


def test_get_second(monkeypatch):
    # Simulamos la entrada del usuario (caso con varios estudiantes con el segundo puntaje más bajo)
    user_input = "5\nHarry\n37.21\nBerry\n37.21\nTina\n37.2\nAkriti\n41\nHarsh\n39\n"

    # Redirigir la entrada estándar (stdin)
    monkeypatch.setattr("sys.stdin", StringIO(user_input))

    # Ejecutar la función
    result = get_second()

    # Verificar que el resultado sea correcto (los nombres con el segundo puntaje más bajo)
    assert result == ["Berry", "Harry"]
