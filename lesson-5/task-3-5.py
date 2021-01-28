with open('task-3.txt', encoding='utf-8') as my_file:
    salary_list = []

    for line in my_file:
        worker_salary = int(line.split()[1])
        salary_list.append(worker_salary)

        if worker_salary < 20000:
            print(f'{line.split()[0]} имеет оклад менее 20 тыс. - {worker_salary}')

print(f'Средняя величина дохода сотрудников - {sum(salary_list) / len(salary_list)}')
