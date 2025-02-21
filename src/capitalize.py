def solve(s):
    result = []
    capitalize_next = True

    for char in s:
        if char == " ":
            capitalize_next = True
        elif capitalize_next:
            char = char.upper()
            capitalize_next = False

        result.append(char)

    return "".join(result)