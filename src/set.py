def me_la_vuela(total_numbers, numbers, total_commands, commands):
    total_numbers = int(total_numbers)
    numbers = set(map(int, numbers.split()))
    total_commands = int(total_commands)
    commands = commands.split(",")

    if len(numbers) == total_numbers and total_commands == len(commands):
        for i in commands:
            try:
                new_command = i.split()

                if new_command[0] == "discard":
                    number_to_discard=int(new_command[1])
                    numbers.discard(number_to_discard)
                    print(numbers)
                if new_command[0] == "remove":
                    number_to_remove=int(new_command[1])
                    numbers.remove(number_to_remove)
                    print(numbers)
                if new_command[0] == "pop":
                    numbers.pop()
                    print(numbers)

            except KeyError as e:
                continue


            except ValueError as e:
                continue

    result = sum(numbers)
    print(result)
    return result



#Refactor:

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input()
    if command == "pop":
        s.pop()
        continue
    word, value = command.split()
    if word == "remove":
        s.remove(int(value))
    elif word == "discard":
        s.discard(int(value))
print(sum(s))
