with open('task-1.txt', 'w') as my_file:
    while True:
        user_text = input('Введите то, что хотите записать в файл. Если закончили - отправьте пустую строку ')
        if user_text == '':
            break
        my_file.write(f'{user_text}\n')
