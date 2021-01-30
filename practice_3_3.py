# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    try:
        my_list = [int(a), int(b), int(c)]
        my_list.sort(reverse=True)
        print(f"{my_list[0]} + {my_list[1]} = {my_list[0] + my_list[1]}")
    except ValueError:
        print("Something goes wrong")
    return


my_func(input("Enter first number: "),
        input("Enter second number: "),
        input("Enter third number: "))
