# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# возведение в степень с помощью оператора **
my_pow1 = lambda a, b: a**b
# возведение в степень с помощью цикла while
def my_pow2(a, b):
    result = 1
    i = 0
    while i < abs(b):
        result /= a
        i += 1
    return result


x = int(input("Enter real positive number: "))
y = int(input("Enter negative integer number: "))
print(my_pow1(x, y))
print(my_pow2(x, y))
