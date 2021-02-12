lessons_count_dict = dict()
unnecessary_elements = [':', '(лаб)', '(пр)', '(л)', ' — ']

with open('task-6.txt', encoding='utf-8') as my_file:
    for line in my_file:
        count = 0

        for element in line.split():
            for i in unnecessary_elements:
                if i in element:
                    new_element = element.replace(i, '')

                    if new_element.isdigit() is True:
                        new_element = int(new_element)
                        count = new_element + count

                    elif type(new_element) is str:
                        title = new_element

        lessons_count_dict.update({title: count})

print(lessons_count_dict)
