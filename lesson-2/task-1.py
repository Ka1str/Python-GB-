# 1 задание. Создать список, проверить тип данных, использовать type
my_list = ['hello', 22, 15.5, 23]
print('Список:', my_list)
for el in my_list:
    if type(el) is str:
        print(f'строка: {el}, тип: {type(el)}')
    elif type(el) is int:
        print(f'число: {el}, тип: {type(el)}')
    elif type(el) is float:
        print(f'число с плавающей точкой: {el}, тип: {type(el)}')
    else:
        print('другой тип данных')