from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def calc_tissue_consumption(self):
        pass

    def __add__(self, other):
        return self._tissue_result + other._tissue_result


class Coat(Wear):
    def __init__(self, size):
        self.size = size

    @property
    def calc_tissue_consumption(self):
        self._tissue_result = round((self.size / 6.5 + 0.5), 2)
        return self._tissue_result


class Suit(Wear):
    def __init__(self, height):
        self.height = height

    @property
    def calc_tissue_consumption(self):
        self._tissue_result = 2 * self.height + 0.3
        return self._tissue_result


new_coat = Coat(30)
print(f'Расход ткани для пальто: {new_coat.calc_tissue_consumption}')

new_suit = Suit(50)
print(f'Расход ткани для костюма: {new_suit.calc_tissue_consumption}')

print(f'Общий расход ткани: {new_coat + new_suit}')
