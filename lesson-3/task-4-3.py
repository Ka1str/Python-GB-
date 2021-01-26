# 1 способ
def exponentiation_numbers(x, y):
    """
    возводит x в степень y
    :param x: float
    :param y: int
    :return: float
    """
    if x > 0:
        if y <= 0:
            return print(x ** y)
        else:
            return print('второе число не отрицательное')
    else:
        return print('первое число не положительное')


user_num_1 = float(input('введите действительное положительное число'))
user_num_2 = int(input('введите целое отрицательное число'))
exponentiation_numbers(user_num_1, user_num_2)


# 2 способ
def exponentiation_numbers_another_method(x, y):
    """
    возводит x в степень y
    :param x: float
    :param y: int
    :return: float
    """
    if x > 0:
        if y <= 0:
            z = 0
            result = 1
            while z != y:
                result = result / x
                z -= 1
            return print(result)
        else:
            return print('второе число не отрицательное')
    else:
        return print('первое число не положительное')


user_num_1 = float(input('введите действительное положительное число'))
user_num_2 = int(input('введите целое отрицательное число'))
exponentiation_numbers_another_method(user_num_1, user_num_2)
