# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering.")


class Pen(Stationery):
    def draw(self):
        print("Start rendering...")
        print(f"You've chosen {self.title}")


class Pencil(Stationery):
    def draw(self):
        print("Start rendering?")
        print(f"You draw with {self.title}")


class Handle(Stationery):
    def draw(self):
        print("Start rendering!")
        print(f"You highlight errors with {self.title}")


s1 = Pen('blue pen')
s2 = Pencil('simple pencil')
s3 = Handle('red handle')
s1.draw()
s2.draw()
s3.draw()
