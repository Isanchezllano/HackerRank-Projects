def practice_exceptions():
    number_of_test_cases = int(input().strip())

    for _ in range(number_of_test_cases):
        value_a, value_b = input().strip().split()

        try:

            result = int(int(value_a) / int(value_b))


        except ZeroDivisionError as e:
            print(f"Error Code: integer division or modulo by zero")

        except ValueError as ve:

            print(f"Error Code: {ve}")

        else:
            print(result)
