# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    msg = 'Divisor is zero'


try:
    while True:
        dividend = int(input("Dividend: "))
        divisor = int(input("Divisor: "))
        if divisor == 0:
            raise MyZeroDivisionError
        print(dividend / divisor)
except MyZeroDivisionError as err:
    print(err.msg)
