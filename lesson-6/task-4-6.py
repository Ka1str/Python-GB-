class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'машина поехала'

    def stop(self):
        return 'машина остановилась'

    def turn(self, direction):
        return f'машина повернула {direction}'

    def show_speed(self):
        return f'текущая скорость: {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Ваша скорость - {self.speed}. Вы превысили допустимую скорость - 60'
        else:
            return f'текущая скорость: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Ваша скорость - {self.speed}. Вы превысили допустимую скорость - 40'
        else:
            return f'текущая скорость: {self.speed}'


class PoliceCar(Car):
    pass


town_car = TownCar(50, 'yellow', 'BMW', False)
print(f'{town_car.name}, цвет - {town_car.color}, полицейская - {town_car.is_police}')
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn('налево'))
print(town_car.stop())

print('')

sport_car = SportCar(60, 'black', 'Mazda', False)
print(f'{sport_car.name}, цвет - {sport_car.color}, полицейская - {sport_car.is_police}')
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn('налево'))
print(sport_car.stop())

print('')

work_car = WorkCar(70, 'green', 'Ford', False)
print(f'{work_car.name}, цвет - {work_car.color}, полицейская - {work_car.is_police}')
print(work_car.go())
print(work_car.turn('направо'))
print(work_car.show_speed())
print(work_car.stop())

print('')

police_car = PoliceCar(50, 'white', 'MB', True)
print(f'{police_car.name}, цвет - {police_car.color}, полицейская - {police_car.is_police}')
print(police_car.go())
print(police_car.show_speed())
print(police_car.turn('направо'))
print(police_car.stop())
