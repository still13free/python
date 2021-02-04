# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.color} {self.name} started")

    def stop(self):
        print(f"{self.color} {self.name} stopped")

    def turn(self, direction):
        print(f"{self.color} {self.name} turned {direction}")

    def show_speed(self):
        print(f"Current speed of {self.color} {self.name} is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Over speed!")
        print(f"Current speed of {self.color} {self.name} is {self.speed}")


class SportCar(Car):
    def go(self):
        print(f"{self.color} {self.name} drove out!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Over speed!")
        print(f"Current speed of {self.color} {self.name} is {self.speed}")

    def do_work(self):
        self.stop()
        print("Doing work...")


class PoliceCar(Car):
    is_police = True

    def go(self):
        print(f"{self.color} {self.name} in patrol")

    def stop(self):
        print(f"{self.color} {self.name} returned to base")

    def pursuit(self, car):
        print(f"{self.color} {self.name} chase {car.color} {car.name}!")


tc1 = TownCar(50, 'Red', 'Nissan March')
tc2 = TownCar(90, 'Yellow', 'Chevrolet Camaro')
sc = SportCar(120, 'Orange', 'Lotus Evora')
wc = WorkCar(30, 'Blue', 'Tractor "Belarus"')
pc1 = PoliceCar(60, 'Police', "Ford Focus")
pc2 = PoliceCar(125, 'Police', "Dodge Charger")

print(tc1.color, tc1.name, tc1.speed, tc1.is_police)
tc1.go()
tc1.show_speed()
tc1.turn('right')
tc1.stop()
print()

tc2.go()
tc2.show_speed()
pc1.go()
pc1.show_speed()
tc2.turn('left')
pc1.pursuit(tc2)
pc1.speed = 110
pc1.show_speed()
print()

wc.go()
wc.do_work()
print()

sc.go()
sc.show_speed()
pc2.pursuit(sc)
