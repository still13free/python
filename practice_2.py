# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_1 = ['string variable', 1258, True, -95.74, 'something else', complex(-4, 7.8), ['', 0, None], False]
i = 0
while i < len(list_1):
    print("{e} - {t}".format(e=list_1[i], t=type(list_1[i])))
    i += 1

# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_2 = []
count = int(input("Enter number of elements: "))
i = 0
while i < count:
    list_2.append(input("Enter {}-element: ".format(i)))
    i += 1
print(list_2)
if count != 1:
    i = 1
    while i < count:
        list_2[i - 1], list_2[i] = list_2[i], list_2[i - 1]
        i += 2
print(list_2)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Enter month-number: "))
# Решение через list
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
if number in winter_list:
    print("It is winter month!")
elif number in spring_list:
    print("It is spring month!")
elif number in summer_list:
    print("It is summer month!")
elif number in autumn_list:
    print("It is autumn month!")
else:
    print("It is strange month. Check yourself!")
# Решение через dict
month_seasons = {1: 'winter',
                 2: 'winter',
                 3: 'spring',
                 4: 'spring',
                 5: 'spring',
                 6: 'summer',
                 7: 'summer',
                 8: 'summer',
                 9: 'autumn',
                 10: 'autumn',
                 11: 'autumn',
                 12: 'winter',
                 }
if number in month_seasons.keys():
    print("It is {} month!".format(month_seasons[number]))
else:
    print("It is strange month. Check yourself!")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

input_str = input("Enter a string of several words, separated by spaces: ")
list_4 = input_str.split()
i = 0
for word in list_4:
    i += 1
    if len(word) > 10:
        print(i, word[:10])
    else:
        print(i, word)

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде.

list_5 = [7, 5, 3, 3, 2]
while True:
    new_el = input("Enter new element: ")
    if new_el.isdigit():
        new_el = int(new_el)
        count = len(list_5)
        for el in list_5:
            if new_el > el:
                list_5.insert(list_5.index(el), new_el)
                break
        if count == len(list_5):
            list_5.append(new_el)
        print(list_5)
    else:
        print("You've entered NaN.")
        break
