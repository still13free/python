# Вариант решения с защитой от некорректного ввода

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    my_list = list(text)
    new_text = ''
    for symbol in my_list:
        if ord(symbol) < ord('a') or ord(symbol) > ord('z'):
            print("There is an impostor among small latin letters!")
            return None
        elif new_text == '':
            new_text = symbol.upper()
        else:
            new_text += symbol
    return new_text


print(int_func(input("Enter one word: ")))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func_ext(text):
    word_list = text.split()
    new_text = ''
    for word in word_list:
        new_word = int_func(word)
        if new_word:
            if new_text == '':
                new_text = new_word
            else:
                new_text += ' ' + new_word
        else:
            print("At least one impostor among us!")
            return None
    return new_text


print(int_func_ext(input("Enter several words: ")))
