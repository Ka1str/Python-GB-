class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f'Невозможно добавить товар на склад:\n {text}'


class TransferWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f'Ошибка прередачи оборудования:\n {text}'


class Warehouse:
    def __init__(self):
        self.__warehouse = []

    def add_equipment(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddWarehouseError(f'Вы пытаетесь добавить на склад не оргтехнику')

        self.__warehouse.extend(equipments)

    def transfer(self, id: int, subdivision: str):
        if not isinstance(id, int):
            raise TransferWarehouseError(f'Недопустимый тип "{type(item)}"')

        item: OfficeEquipment = self.__warehouse[id]

        if item.subdivision:
            raise TransferWarehouseError(f'Оборудование {item} уже закреплено за отделом {item.subdivision}')

        item.subdivision = subdivision

    def filter_by(self, **kwargs):
        for index, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield index, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__warehouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__warehouse[key]

    def __iter__(self):
        return self.__warehouse.__iter__()

    def __str__(self):
        return f'На складе сейчас {len(self.__warehouse)} устройств'


class OfficeEquipment:
    __required_props = ('equipment_type', 'model', 'color')

    def __init__(self, equipment_type, model, color):
        self.type = equipment_type
        self.model = model
        self.color = color
        self.subdivision = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f'"{key}" должен иметь значение отличное от false')

        object.__setattr__(self, key, value)

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f'{self.type} {self.model}, color: {self.color}'

    @staticmethod
    def validate(count):
        if not isinstance(count, int):
            raise TypeError(f'"{count}" должно быть "int"')

    @classmethod
    def create(cls, count, **properties):
        cls.validate(count)
        return [cls(**properties) for _ in range(count)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(equipment_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(equipment_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(equipment_type='Xerox', **kwargs)


my_warehouse = Warehouse()
my_warehouse.add_equipment(Printer.create(2, model='HP LaserJet 1018', color='white'))
my_warehouse.add_equipment(Scanner.create(5, model='Canon imageFORMULA DR-C230', color='black'))
my_warehouse.add_equipment(Xerox.create(3, model='B1025', color='black/white'))

for id, item in my_warehouse.filter_by(subdivision=None, model='HP LaserJet 1018', color='white'):
    print(f'Перемещаем {item} в подразделение "Some Division"')
    my_warehouse.transfer(id, 'Some Division')
print('')
print('Список устройств подразделения "Some Division":')

for id, item in my_warehouse.filter_by(subdivision='Some Division'):
    print(id, f'{item} не распределены по подразделениям')

print('')
print('Список устройств без подразделения:')

for id, item in my_warehouse.filter_by(subdivision=None):
    print(id, f'{item} не распределены по подразделениям')

print('')
print(my_warehouse)
print('Списываем 1 устройство')
del my_warehouse[0]
print(my_warehouse)
