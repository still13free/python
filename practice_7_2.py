# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    name = None

    @abstractmethod
    def tissue(self):
        pass

    @abstractmethod
    def tissue_with(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.V = size

    @property
    def tissue(self):
        return round(self.V / 6.5 + 0.5, 2)

    def tissue_with(self, other):
        return round(self.V / 6.5 + 0.5 + other.H * 2 + 0.3, 2)


class Costume(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.H = height

    @property
    def tissue(self):
        return round(self.H * 2 + 0.3, 2)

    def tissue_with(self, other):
        return round(other.V / 6.5 + 0.5 + self.H * 2 + 0.3, 2)


coat_1 = Coat('Coat #1', 52)
coat_2 = Coat('Coat #2', 64)
costume = Costume('Costume', 1.80)
print("Amount of tissue required for production", coat_1.name, coat_1.tissue)
print("Amount of tissue required for production", coat_2.name, coat_2.tissue)
print("Amount of tissue required for production", costume.name, costume.tissue)
print(f"Amount of tissue required for production {coat_1.name} and {costume.name}", coat_1.tissue_with(costume))
print(f"Amount of tissue required for production {costume.name} and {coat_2.name}", costume.tissue_with(coat_2))
