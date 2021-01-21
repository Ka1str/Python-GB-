def print_numbers_sum(num_1, num_2, num_3):
    """
    Возвращает сумму наибольших двух чисел из трех
    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: print сумма наибольших двух (int)
    """
    num_list = sorted([num_1, num_2, num_3], reverse=True)
    return print(num_list[0] + num_list[1])


user_num_1 = int(input('введите первое число'))
user_num_2 = int(input('введите второе число'))
user_num_3 = int(input('введите третье число'))
print_numbers_sum(user_num_1, user_num_2, user_num_3)
