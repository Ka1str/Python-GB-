my_file = open('task-4.txt', 'r', encoding='utf-8')
my_new_file = open('task-4-1.txt', 'w', encoding='utf-8')

num_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0

for line in my_file:
    new_line = line.replace(line.split()[0], num_list[i])
    my_new_file.write(new_line)
    i += 1

my_file.close()
my_new_file.close()
