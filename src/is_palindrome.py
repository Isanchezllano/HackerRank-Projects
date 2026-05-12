def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    number = str(x)

    return number == number[::-1]

