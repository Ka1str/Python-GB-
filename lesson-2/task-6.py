# 6 задание. Реализовать структуру данных «Товары»
user_answer = int(input('сколько товаров хотите добавить:'))
i = 1
product_list = []
name_list = []
price_list = []
count_list = []
unit_list = []
all_dict = dict()
while user_answer >= i:
    name = input(f'название товара №{i} ')
    price = int(input(f'цена товара №{i} '))
    count = int(input(f'количество товара №{i} '))
    unit = input(f'единица измерения №{i} ')
    product_dict = {'название': name, 'цена': price, 'количество': count, 'ед': unit}
    product_cort = (i, product_dict)
    product_list.append(product_cort)
    print('')
    i += 1
for result in product_list:
    print(result)
for number, product in product_list:
    name_list.append(product['название'])
    price_list.append(product['цена'])
    count_list.append(product['количество'])
    unit_list.append(product['ед'])
all_dict.update({'название': name_list})
all_dict.update({'цена': price_list})
all_dict.update({'количество': count_list})
all_dict.update({'ед': list(set(unit_list))})
print(all_dict)
for key, val in all_dict.items():
    print(f'{key}: {val}')