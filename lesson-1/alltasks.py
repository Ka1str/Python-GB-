#Задание1
print('Задание 1. Вывести на экран переменные')
number = 1
task = 'Задание'
print(task, number)
user_text = input('Введите текст:')
user_number = int(input('Введите целое число:'))
user_fraction_number = float(input('Введите число с плавающей запятой:'))
print('Ваш текст:', user_text)
print('Ваше целое число:', user_number)
print('Ваше число с плавающей запятой:', user_fraction_number)

#Задание2
print('Задание 2.Перевести время в часы, минуты и секунды')
user_seconds = int(input('Введите время в секундах:'))
hours = user_seconds // 3600
minutes = (user_seconds // 60) % 60
seconds = user_seconds % 60
print(f'часов:{hours}, минут:{minutes}, секунд:{seconds}')

#Задание3
print('Задание 3. Найти сумму чисел n + nn + nnn')
n = int(input('Введите число n:'))
n = str(n)
nn = n + n
nnn = n + n + n
sum = int(n) + int(nn) + int(nnn)
print(f"{n}+{nn}+{nnn}={sum}")

#Задание4
print('Задание 4. Найти самую большую цифру в числе')
num = int(input('Введите целое положительное число:'))
mx = 0
while num > 0:
    d = num % 10
    if d >= mx:
        mx = d
    num = num // 10
print('Максимальная цифра из числа:', mx)

#Задание5
print('Задание 5. Определить финансовый результат фирмы, рентабельность и прибыль фирмы на одного сотрудника')
proceeds = int(input('Введите выручку:'))
outgoings = int(input('Введите издержки:'))
if proceeds > outgoings:
    profit = proceeds - outgoings
    print('У Вас прибыль, которая составляет:', profit)
    profitability = float(profit / proceeds * 100)
    print('Рентабельность: {:.2f}%'.format(profitability))
    worker_count = int(input('Введите кол-во работников:'))
    worker_profit = float(profit / worker_count)
    print('Прибыль на одного работника: {:.2f}'.format(worker_profit))
elif proceeds == outgoings:
    print('Выручка равна издержкам')
elif proceeds < outgoings:
    losses = outgoings - proceeds
    print('У Вас убыток, который равен:', losses)

#Задание6
print('Задание 6. Определить номер дня, на который общий результат спортсмена составит не менее b километров')
a = int(input('Сколько километров спортсмен пробежал в первый день:'))
b = int(input('Сколько километров спортсмен должен пробежать:'))
day = 1
result = a
print(f'{day}-й день: {result}')
while a <= b:
    result = a * 0.1 + a
    a = result
    day += 1
    print(f'{day}-й день: {result:.2f}')
print(f'на {day}-й день: спортсмен достиг результата - не менее {b} км')