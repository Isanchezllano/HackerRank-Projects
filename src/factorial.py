def get_the_factorial(number):

    if number == 0 or number == 1:  # Caso base
        return 1
    return number * get_the_factorial(number - 1)  # Llamada recursiva


if __name__=="__main__":
    print(get_the_factorial(5))