# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    return text.capitalize()


print(int_func(input("Enter one word: ")))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func_ext(text):
    word_list = text.split()
    new_text = ''
    for word in word_list:
        if new_text == '':
            new_text = int_func(word)
        else:
            new_text += ' ' + int_func(word)
    return new_text


print(int_func_ext(input("Enter several words: ")))
