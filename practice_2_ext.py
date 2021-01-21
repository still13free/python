# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

print("_____________Data structure «Products»_____________")
print("_________{Enter 'e' to enter new product}__________")
print("_________{Enter 'a' to analyze products}___________")
print("_{Leave the field blank and press 'Enter' to exit}_")
list_6 = list()
i = 0
while True:
    user_action = input(">")
    if user_action == '':
        break
    if user_action.lower() == 'e':
        i += 1
        new_name = input("Enter new product name: ")
        new_price = float(input("Enter new product price: "))
        new_amount = int(input("Enter new product amount: "))
        new_m_unit = input("Enter new product measure unit: ")
        new_product = (i, dict(name=new_name, price=new_price, amount=new_amount, m_unit=new_m_unit))
        list_6.append(new_product)
        print("New product added: {name} in amount {amount}{m_unit} by price {price}$ per {m_unit}".format(
            name=new_name, price=new_price, amount=new_amount, m_unit=new_m_unit))
        print()
    if user_action.lower() == 'a':
        if i == 0:
            print("You've don't added any product yet!")
        else:
            names = set()
            prices = set()
            amounts = set()
            m_units = set()
            for product in list_6:
                names.add(product[1].get('name'))
                prices.add(product[1].get('price'))
                amounts.add(product[1].get('amount'))
                m_units.add(product[1].get('m_unit'))
            print("List of product names:", names)
            print("List of product prices:", prices)
            print("List of product amounts:", amounts)
            print("List of product measure units:", m_units)
        print()
