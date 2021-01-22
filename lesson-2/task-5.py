# 5 Задание. Реализовать структуру «Рейтинг»
my_list = [7, 5, 3, 3, 2]
i = 0
a = len(my_list) - 1
print('Рейтинг:', my_list)
user_num = int(input('Введите новый элемент рейтинга:'))
while i <= len(my_list):
    if user_num > my_list[i]:
        my_list.insert(i, user_num)
        break
    elif user_num <= my_list[a]:
        my_list.append(user_num)
        break
    i += 1
print('Новый рейтинг:', my_list)