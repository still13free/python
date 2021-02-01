# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('textfile_5_5.txt', 'w') as my_file:
    print(input("Enter some numbers separated by spaces: "), file=my_file)

with open('textfile_5_5.txt') as my_file:
    numbers = my_file.readline().split()
    summary = 0
    for number in numbers:
        summary += int(number)
    print("Sum of entered numbers:", summary)