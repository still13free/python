# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('textfile_5_2.txt', 'r')
count = 0
while True:
    line = my_file.readline()
    if not line:
        break
    count += 1
    words = len(line.split())
    print(f"Line {count} has {words} words")
print(f"There is {count} lines")