class Date:

    def __init__(self, user_date):
        self.user_date = user_date
        self.day = (self.get_number(self.user_date))[0]
        self.month = (self.get_number(self.user_date))[1]
        self.year = (self.get_number(self.user_date))[2]
        if self.validate(self.day, self.month, self.year) is False:
            raise ValueError('Некорректная дата')

    @classmethod
    def get_number(cls, user_date):
        date_parts = user_date.split('-')
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'Текущая дата: {self.day}.{self.month}.{self.year}'


my_date = Date(input('Введите дату в виде строки формата «день-месяц-год»'))
print(my_date)
new_date = Date(input('Введите другую дату в виде строки формата «день-месяц-год»'))
print(new_date)
print('')
print(Date.get_number('15-01-2020'))
print(Date.validate(30, 13, 2020))
