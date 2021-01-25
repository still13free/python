# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum():
    result = 0
    # позволяем пользователю самому определить специальный символ
    stop_symbol = ''
    # но не разрешаем вводить более одного символа или цифру
    while len(stop_symbol) != 1 or stop_symbol.isdigit():
        stop_symbol = input("Enter stop symbol: ")
    go = True
    while go:
        my_list = input("Enter integer numbers separated by spaces: ").split()
        for number in my_list:
            if number != stop_symbol:
                try:
                    result += int(number)
                except ValueError:
                    print("You've entered not a number or stop symbol!")
            else:
                go = False
                break
        print(f"Sum of all entered numbers is {result}")
    return


my_sum()
