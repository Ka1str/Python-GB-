class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркером'


my_pen = Pen('ручка')
print(my_pen.title)
print(my_pen.draw())

my_pencil = Pencil('карандаш')
print(my_pencil.title)
print(my_pencil.draw())

my_handle = Handle('маркер')
print(my_handle.title)
print(my_handle.draw())
