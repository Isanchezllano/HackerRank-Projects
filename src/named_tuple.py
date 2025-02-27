from collections import namedtuple


def get_mark_student_average():
    students = int(input())
    columns = input()
    Student = namedtuple('Student', columns)

    sum_of_all_marks = 0

    for _ in range(students):
        student_data = input().strip().split()
        student = Student(*student_data)

        sum_of_all_marks += int(student.MARKS)

    print(sum_of_all_marks / students)
