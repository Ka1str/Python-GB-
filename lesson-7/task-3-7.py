class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        count_result = self.count - other.count

        if count_result > 0:
            return count_result

        return 'недопустимая операция'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, count_in_row: int):
        rows = self.count // count_in_row
        remainder = self.count % count_in_row
        return '\n'.join(['*' * count_in_row] * rows + (['*' * remainder] if remainder != 0 else []))


a = Cell(50)
b = Cell(20)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b.make_order(6))
