from is_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome(0) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(121) == True
    assert is_palindrome(5) == True