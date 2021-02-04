# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 15}

    def running(self):
        for color, secs in cycle(self.__color.items()):
            print(f"Turn on {color} light!")
            for i in range(secs):
                print(secs - i)
                sleep(1)


tl = TrafficLight()
tl.running()
