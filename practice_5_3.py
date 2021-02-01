# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('textfile_5_3.txt') as my_file:
    sum_salary = 0
    for line in my_file:
        name, salary = line.split()
        salary = int(salary)
        sum_salary += salary
        if salary < 20000:
            print(f"{name} has salary less than 20000.")
    my_file.seek(0)
    average_salary = sum_salary / len(my_file.readlines())
    print(f"Average salary is {average_salary}")
