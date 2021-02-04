# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLightExt:
    __color = {'red': 7, 'yellow': 2, 'green': 15}

    def running(self):
        previous_light = None
        while True:
            color = input('Enter color you want to turn on: ')
            if (previous_light is None or
                    previous_light == 'red' and color == 'yellow' or
                    previous_light == 'yellow' and color == 'green' or
                    previous_light == 'green' and color == 'red'):
                self.__turn_light_on(color)
                previous_light = color
            else:
                print('Incorrect sequence')
                break

    def __turn_light_on(self, color):
        print(f"Turn on {color} light!")
        secs = self.__color.get(color)
        for i in range(secs):
            print(secs - i)
            sleep(1)


tle = TrafficLightExt()
tle.running()
