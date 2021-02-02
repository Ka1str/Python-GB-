class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self):
        square_meter_mass = 25
        thickness = 5
        result = self._length * self._width * square_meter_mass * thickness
        return print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна - {result / 1000}т')


new_road = Road(20, 5000)
new_road.get_asphalt_mass()
