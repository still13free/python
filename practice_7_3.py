# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            raise ArithmeticError('You are trying to subtract more cells than there are!')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, cells_per_row):
        order = ''
        cells_in_row = 0
        for i in range(self.number):
            if cells_in_row == cells_per_row:
                order += '\n'
                cells_in_row = 0
            order += '*'
            cells_in_row += 1
        return order

    def make_order2(self, cells_per_row):
        number = self.number
        order = ''
        while number > cells_per_row:
            order += '*' * cells_per_row + '\n'
            number -= cells_per_row
        return order + '*' * number


c1 = Cell(int(input('Enter the number of first cell:')))
c2 = Cell(int(input('Enter the number of second cell:')))

print("Addition:", (c1 + c2).number)
print("Subtraction:", (c1 - c2).number)
print("Multiplication:", (c1 * c2).number)
print("Division:", (c1 / c2).number)
print(c1.make_order(int(input('Enter the number of first cell order:'))))
print(c2.make_order(int(input('Enter the number of second cell order:'))))
print(c2.make_order2(int(input('Enter the number of second cell order2:'))))
