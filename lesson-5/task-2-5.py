with open('task-2.txt') as my_file:
    print('Количество строк: ', len(my_file.readlines()))

    my_file.seek(0)

    i = 1

    for line in my_file:
        print(f'Количество слов в {i} строке - {len(line.split())}')
        i += 1
