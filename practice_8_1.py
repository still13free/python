# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day, self.month, self.year = Date.get_number(day_month_year)

    @classmethod
    def get_number(cls, day_month_year):
        numbers = day_month_year.split('-')
        for i, number in enumerate(numbers):
            numbers[i] = int(number)
        Date.check_date(numbers)
        return numbers

    @staticmethod
    def check_date(numbers_list):
        month_31 = [1, 3, 5, 7, 8, 10, 12]
        month_30 = [4, 6, 9, 11]
        day, month, year = numbers_list
        if year in range(3000):
            if 1 <= month <= 12:
                if (month in month_31 and 1 <= day <= 31 or
                        month in month_30 and 1 <= day <= 30 or
                        year % 4 == 0 and 1 <= day <= 29 or 1 <= day <= 28):
                    print("Correct date")
                else:
                    print("Incorrect day:", day)
            else:
                print("Incorrect month:", month)
        else:
            print("Incorrect year:", year)
        print(numbers_list)


date = Date('15-01-1996')
date = Date('15-01-3000')
date = Date('15-13-2020')
date = Date('30-02-2020')
date = Date('29-02-2020')
date = Date('29-02-2021')

date.get_number('15-01-1996')
date.check_date([15, 1, 1996])
Date.get_number('15-01-1996')
Date.check_date([15, 1, 1996])
