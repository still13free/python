# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(var1, var2):
    try:
        result = var1 / var2
        print(f"{var1} / {var2} = {result}")
    except ZeroDivisionError:
        print("Fault! You've tried divide by zero!")
    return None


a1 = int(input("Enter dividend:"))
b1 = int(input("Enter quotient:"))
my_division(a1, b1)
