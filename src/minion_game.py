def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = "aeiouAEIOU"
    length = len(string)

    for i, letter in enumerate(string):
        if letter in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        result = f"Stuart {stuart}"
    elif kevin > stuart:
        result = f"Kevin {kevin}"
    else:
        result = "Draw"

    return result


minion_game("BANANA")
a=10

    # also y have to count all the vowels and consonants

    # i have to iterar over the string and if there is a vowel, do a slicing starting with the vowel


# i need to search for substring that starts with vowels and consonants



