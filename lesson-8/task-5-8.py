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

    def add_equipment(self, item: 'OfficeEquipment'):
        if not isinstance(item, OfficeEquipment):
            raise AddWarehouseError(f'{item} не оргтехника')

        self.__warehouse.append(item)

    def transfer(self, index: int, subdivision: str):
        if not isinstance(index, int):
            raise TransferWarehouseError(f'Недопустимый тип "{type(item)}"')

        item: OfficeEquipment = self.__warehouse[index]

        if item.subdivision:
            raise TransferWarehouseError(f'Оборудование {item} уже закреплено за отделом {item.subdivision}')

        item.subdivision = subdivision

    def filter_by(self, **kwargs):
        for index, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
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

    def __init__(self, type, model, color):
        self.type = type
        self.model = model
        self.color = color
        self.subdivision = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f'{self.type} {self.model}, color: {self.color}'


class Printer(OfficeEquipment):
    def __init__(self, *args):
        self.equipment_type = 'Printer'
        super().__init__(self.equipment_type, *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        self.equipment_type = 'Scanner'
        super().__init__(self.equipment_type, *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        self.equipment_type = 'Xerox'
        super().__init__(self.equipment_type, *args)


my_printer = Printer('HP LaserJet 1018', 'white')
print(my_printer)
my_scanner = Scanner('Canon imageFORMULA DR-C230', 'black')
print(my_scanner)
my_xerox = Xerox('B1025', 'white/black')
print(my_xerox)

my_warehouse = Warehouse()
my_warehouse.add_equipment(my_printer)
my_warehouse.add_equipment(my_scanner)
my_warehouse.add_equipment(my_xerox)

last_id = None
for id, itm in my_warehouse.filter_by(subdivision=None):
    print(id, itm)
    last_id = id

print('Перемещаем последнее устройство в подразделение Some Division')
my_warehouse.transfer(last_id, 'Some Division')

for id, itm in my_warehouse.filter_by(subdivision='Some Division'):
    print(f'В подразделении "Some Division": \n{id} {itm}')

print(my_warehouse)
print('Удаляем последнее устройство')
del my_warehouse[last_id]
print(my_warehouse)
