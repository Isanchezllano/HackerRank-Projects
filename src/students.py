def get_second():
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])

    min_score = students[0][1]

    second_min = None

    for name, score in students:
        if score > min_score:
            second_min = score
            break

    name_second = [name for name, score in students if score == second_min]

    name_second.sort()

    return name_second

if __name__=="__main__":
    print(get_second())

# I need to stop when that function has actualized the second.


# I have to select first sublist witch the second element is bigger than the second element of the fisrt sublist.
