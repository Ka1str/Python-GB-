def print_numbers_sum():
    """
    Печатает сумму чисел пользователя
    При "@" прекращает работу
    """
    temp_list = []
    control = True
    while control:
        user_nums = input('введите числа через пробел; введите "@", чтобы прекратить').split()
        for val in user_nums:
            if '@' in val:
                control = False
                break
            temp_list.append(int(val))
        print(sum(temp_list))


print_numbers_sum()
