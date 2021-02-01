# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('textfile_5_7.txt') as firm_data:
    firms = {}
    firms_in_profit = 0
    sum_profit = 0
    for line in firm_data:
        name, ownership_form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms.update({name: profit})
        if profit > 0:
            sum_profit += profit
            firms_in_profit += 1
    average_profit = int(sum_profit / firms_in_profit)
    total_list = [firms, {'average_profit': average_profit}]

with open('jsonfile_5_7.json', 'w') as jsonfile:
    json.dump(total_list, jsonfile)
