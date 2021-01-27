# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

my_list = [-13, "hello!", None, 7.62, True]
try:
    start = int(input("Enter start number: "))
    stop = int(input("Enter stop number: "))
    # итератор, генерирующий целые числа
    for i in count(start):
        print(i)
        if i == stop:
            break
    # итератор, повторяющий элементы списка
    c = start
    for i in cycle(my_list):
        print(i)
        if c == stop:
            break
        c += 1
except ValueError:
    print("You've enter NaN")
