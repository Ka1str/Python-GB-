from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            sleep(7)

            self.__color = 'Желтый'
            print(self.__color)
            sleep(2)

            self.__color = 'Зеленый'
            print(self.__color)
            sleep(15)


new_traffic_light = TrafficLight()
new_traffic_light.running()
