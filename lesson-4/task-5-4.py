from functools import reduce


def multiply_func(prev_el, el):
    """
    Умножает предыдущий элемент на текущий
    :param prev_el: предыдущий элемент
    :param el: текущий элемент
    :return: prev_el * el
    """
    return prev_el * el


num_list = [num for num in range(100, 1001) if num % 2 == 0]

result = reduce(multiply_func, num_list)
print(result)
