def divide_numbers(num_1, num_2):
    """
    Деление одного числа на другое
    :param num_1: float
    :param num_2: float
    есть ZeroDivisionError
    :return: при num_1 % num_2 == 0 возвращаем int, в др случаях float
    """
    try:
        result = num_1 / num_2
        if num_1 % num_2 == 0:
            result = int(result)
            return print(result)
        else:
            return print(round(result, 2))
    except ZeroDivisionError:
        print('делить на ноль нельзя')


user_num_1 = float(input('Введите первое число'))
user_num_2 = float(input('Введите второе число'))
divide_numbers(user_num_1, user_num_2)
