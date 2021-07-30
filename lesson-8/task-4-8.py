class Warehouse:
    pass


class OfficeEquipment:

    def __init__(self, type, model, color):
        self.type = type
        self.model = model
        self.color = color

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
