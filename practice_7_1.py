# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, value):
        self.matrix = value
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def __str__(self):
        str_matrix = ''
        for rows in self.matrix:
            for el in rows:
                str_matrix += f'{el:>3}'
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            new_matrix = list()
            for i, rows in enumerate(self.matrix):
                new_row = list()
                for j, el in enumerate(rows):
                    new_row.append(el + other.matrix[i][j])
                new_matrix.append(new_row)
            return Matrix(new_matrix)
        else:
            raise ArithmeticError('Incorrect addition. Please check the dimensions of matrix')

    def __len__(self):
        return self.rows * self.columns


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 6, 14], [-1, 4, -7], [1, 0, -1]])
print(m1)
print(m2)
print(m1 + m2)
m3 = Matrix([[1, 2, 3], [7, 8, 9]])
m4 = Matrix([[-1, 4, -7], [1, 0, -1]])
print(m3)
print(m4)
print(m3 + m4)
m5 = Matrix([[1, 3], [5, 6], [7, 9]])
m6 = Matrix([[9, -4], [-1, -7], [1, 0]])
print(m5)
print(m6)
print(m5 + m6)
