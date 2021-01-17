# 4 задание. Пронумеровать список. Если слово длинное, выводить только первые 10 букв в слове
user_answer = input('Что хотите добавить в список? Элементы списка пишите через пробел ').split()
print(user_answer)
for ind, el in enumerate(user_answer, 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)