my_file = open('task-5.txt', 'w')
user_numbers = input('Введите числа через пробел ').split()

my_file.writelines('%s\n' % user_number for user_number in user_numbers)
my_file.close()

file = open('task-5.txt', 'r')
numbers = []

for number in file:
    number = int(number)
    numbers.append(number)

print(f'Сумма чисел - {sum(numbers)}')
file.close()
