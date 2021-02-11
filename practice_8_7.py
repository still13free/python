# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return f'({self.re}{self.im}i)'
        else:
            return f'({self.re}+{self.im}i)'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


c1 = Complex(1, -4)
c2 = Complex(-3, 2)
bc1 = complex(1, -4)
bc2 = complex(-3, 2)
print('class Complex addition:', c1 + c2)
print('built-in complex addition:', bc1 + bc2)
print('class Complex multiplication:', c1 * c2)
print('built-in complex multiplication:', bc1 * bc2)
