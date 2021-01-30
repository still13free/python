# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(var1, var2):
    try:
        result = var1 / var2
        return f"{var1} / {var2} = {result}"
    except ZeroDivisionError:
        return "Fault! You've tried divide by zero!"


a = int(input("Enter dividend:"))
b = int(input("Enter divider:"))
print(my_division(a, b))
