from set import me_la_vuela


def test_me_la_vuela():
    total_numbers = "9"
    numbers= "1 2 3 4 5 6 7 8 9"
    total_commands = "10"
    commands= "pop, remove 9, discard 9, discard 8, remove 7, pop, discard 6, remove 5, pop, discard 5"

    result = me_la_vuela(total_numbers, numbers, total_commands, commands)

    assert result == 4



