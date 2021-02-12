class NotNumber(Exception):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def check_for_num(value):
        if value.isdigit():
            return True
        else:
            return False

    def __str__(self):
        return self.text


num_list = []

while True:
    user_input = input('Введите число для заполнения списка, "stop" для выхода: ')

    if user_input == "stop":
        break

    try:
        if NotNumber.check_for_num(user_input) is True:
            num_list.append(int(user_input))
        else:
            raise NotNumber(f'"{user_input}" не является числом')

    except NotNumber as error:
        print(error)

print(num_list)
