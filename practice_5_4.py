# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_lines = []

with open('textfile_5_4_old.txt', encoding='utf-8') as old_file:
    for line in old_file:
        words = line.split()
        for i, word in enumerate(words):
            if word in translation.keys():
                words[i] = translation.get(word)
        new_lines.append(" ".join(words))

with open('textfile_5_4_new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write('\n'.join(new_lines))
