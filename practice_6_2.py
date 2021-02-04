# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        """
        :param length: measured in meters (m)
        :param width: measured in meters (m)
        """
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, mass_per_cm, thickness):
        """
        :param mass_per_cm: mass of asphalt for covering one square meter of the road with 1 cm thick asphalt,
                            measured in kilograms (kg)
        :param thickness: asphalt canvas thickness, measured in centimeters (cm)
        :return: mass of asphalt required to cover the entire roadway, measured in tons
        """
        return self._width * self._length * mass_per_cm * thickness / 1000


r1 = Road(20, 5000)
print(r1.calc_asphalt_mass(25, 5))
