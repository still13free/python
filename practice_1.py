# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var_1 = 13
var_2 = -7.62
var_3 = "variable"
print(var_1)
print(var_2)
print(var_3)
invar_1 = int(input("Enter integer number: "))
invar_2 = float(input("Enter float number: "))
invar_3 = input("Enter string: ")
print(invar_1)
print(invar_2)
print(invar_3)

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

s = int(input("Enter time (in seconds): "))
m = s // 60
s = s % 60
h = m // 60
m = m % 60
print("Time is: {hours}:{minutes:2}:{seconds:2}".format(hours=h, minutes=m, seconds=s))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

number = input("Enter number 'n': ")
sum_n = int(number) + int(number + number) + int(number + number + number)
print("n + nn + nnn =", sum_n)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Enter positive integer number: "))
max_digit = 0
while True:
    q = number // 10  # частное целочисленного деления на 10
    r = number % 10  # остаток от деления на 10
    if r > max_digit:
        max_digit = r
    if q > 0:
        number = q
    else:
        break
print("Largest digit in number is", max_digit)

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Enter proceeds: "))
expenses = float(input("Enter expenses: "))
fin_result = proceeds - expenses
if fin_result > 0:
    print("The firm works in profit!")
    print("Profitability of proceeds: {:.2f}".format(fin_result / proceeds))
    count = int(input("Enter number of employees: "))
    print("Firm profit per employee: {:.2f}".format(fin_result / count))
else:
    print("The firm is operating at a loss!")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил 'a' километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее 'b' километров.
# Программа должна принимать значения параметров 'a' и 'b' и выводить одно натуральное число — номер дня.

a = float(input("Enter first day result, 'a': "))
b = float(input("Enter final day result, 'b': "))
i = 1
while a < b:
    a = 1.1 * a
    i += 1
print(i)