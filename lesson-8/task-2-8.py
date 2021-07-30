class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Div(float):
    def __truediv__(self, other):
        if other == 0.0:
            raise MyZeroDivisionError(f'Деление на ноль запрещено')

        return Div(float(self) / float(other))


while True:
    try:
        dividend, divider = map(Div, input('Введите делимое и делитель через пробел: ').split())
        print(dividend / divider)
    except MyZeroDivisionError as error:
        print(error)
    except ValueError as error:
        print(error)
        break
