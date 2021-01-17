# 2 задание. Обмен значениями соседних элементов

# 1 cпособ
my_list = input('Что хотите добавить в список? Элементы списка пишите через пробел ').split()
print('Ваш список:', my_list)
i = 1
while i <= len(my_list):
    if i == len(my_list):
        break
    a = my_list.pop(i)
    my_list.insert(i - 1, a)
    i += 2
print('Список с обменом значений:', my_list)

# 2 способ
# my_list = input('Что хотите добавить в список? Элементы списка пишите через пробел ').split()
# print('Ваш список:', my_list)
# i = 0
# new_list = []
#
# while i <= len(my_list):
#     if i == len(my_list):
#         break
#     elif i + 1 == len(my_list):
#         new_list.append(my_list[i])
#         break
#     else:
#         new_list.append(my_list[i + 1])
#         new_list.append(my_list[i])
#         i += 2
# print('Список с обменом значений:', new_list)