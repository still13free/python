# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('textfile_5_1.txt', 'w')
while True:
    line = input("Enter something: ")
    if not line:
        break
    my_file.write(line + '\n')
my_file.close()
