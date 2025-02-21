def merge_the_tools(string, k):

    if len(string) % k != 0:
        print("Error")
        return

    block = len(string)//k

    new_string=[string[i:i+block] for i in range (0, len(string), block)]

    non_repeat = ["".join(dict.fromkeys(sub)) for sub in new_string]

    return non_repeat
    # your code goes here


if __name__ == '__main__':
    string, k = input(), int(input())
    a=merge_the_tools(string, k)
    print(a)
