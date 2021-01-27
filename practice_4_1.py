# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def my_salary(hours, rate, bonus):
    return hours * rate + bonus


name, working_hours, monthly_rate, cash_bonus = argv
try:
    salary = my_salary(
        int(working_hours),
        float(monthly_rate),
        float(cash_bonus)
    )
    print(f"You salary is {salary:.2f} rubles")
except ValueError:
    print("You've entered NaN!")
