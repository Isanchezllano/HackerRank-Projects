
def set_remove_discard_pop():
    amount_numbers = int(input())
    numbers_set = set(map(int, input().split()))
    amount_of_commands = int(input())
    for _ in range(amount_of_commands):
        command = input()
        if command == "pop":
            numbers_set.pop()
            continue
        word, value = command.split()
        if word == "remove":
            numbers_set.remove(int(value))
        elif word == "discard":
            numbers_set.discard(int(value))
    print(sum(numbers_set))
