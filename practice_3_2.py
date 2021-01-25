# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_user(name='Nobody', surname='Nothing', year=0000, city='Nowhere', email='adress@none.com', phone=80123456789):
    print(f"{name} {surname} was born in {year}. Nowadays live in {city}.")
    print(f"E-mail: {email}. Phone number: {phone}")


my_user(
    name='Artem',
    #surname='Eremyan',
    year=1996,
    city='Ekaterinburg',
    email='ae96.ekat@mail.ru',
    #phone=83432666666
)
