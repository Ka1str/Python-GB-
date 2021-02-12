class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Имя, фамилия - {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход у учетом премии - {sum(self._income.values())}'


first_person = Position('Юрий', 'Жуков', 'Сантехник', 50000, 5000)
print(f'Имя - {first_person.name}, фамилия - {first_person.surname}, должность - {first_person.position}')
print(first_person.get_full_name())
print(first_person.get_total_income())

print('')

second_person = Position('Игорь', 'Новиков', 'Повар', 80000, 10000)
print(f'Имя - {second_person.name}, фамилия - {second_person.surname}, должность - {second_person.position}')
print(second_person.get_full_name())
print(second_person.get_total_income())
