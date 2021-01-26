def divide_numbers(num_1, num_2):
    """
    Деление одного числа на другое
    :param num_1: float
    :param num_2: float
    есть ZeroDivisionError
    :return: print float
    """
    try:
        result = num_1 / num_2
        return print(round(result, 2))
    except ZeroDivisionError:
        print('делить на ноль нельзя')


user_num_1 = float(input('Введите первое число'))
user_num_2 = float(input('Введите второе число'))
divide_numbers(user_num_1, user_num_2)
