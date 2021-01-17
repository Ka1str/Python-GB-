# 3 задание. Времена года
# list
user_list_month = int(input('Способ решения через list.\nВведите месяц в виде целого числа от 1 до 12:'))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
while user_list_month > 12:
    user_list_month = int(input('Введите месяц в виде целого числа от 1 до 12:'))
if user_list_month in winter:
    print(f'{user_list_month}-й месяц относится к зиме')
elif user_list_month in spring:
    print(f'{user_list_month}-й месяц относится к весне')
elif user_list_month in summer:
    print(f'{user_list_month}-й месяц относится к лету')
elif user_list_month in autumn:
    print(f'{user_list_month}-й месяц относится к осени')

# dict
user_dict_month = int(input('Способ решения через dict.\nВведите месяц в виде целого числа от 1 до 12:'))
my_dict = {'зима':{'Январь': 1, 'Февраль': 2, 'Декабрь': 12},
    'весна':{'Март': 3, 'Апрель': 4, 'Май': 5},
    'лето':{'Июнь': 6, 'Июль': 7, 'Август': 8},
    'осень':{'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11}
}
while user_dict_month > 12:
    user_dict_month = int(input('Введите месяц в виде целого числа от 1 до 12:'))
for key, value in my_dict.items():
    for monthKey, monthValue in value.items():
        if monthValue == user_dict_month:
            print(f'{monthKey} месяц. Время года - {key}')