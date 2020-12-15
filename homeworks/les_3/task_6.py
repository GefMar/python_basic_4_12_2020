# homework lesson: 3, task:6

"""
Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(string: str):
    return ''.join((string[0].upper(), string[1:])) if string else string


def user_temp(string: str):
    return ' '.join(map(int_func, string.split(' ')))


# можно обойтись методом .title()

assert int_func('колбаса') == 'Колбаса', "int_func('колбаса')"
assert int_func('самса') == 'Самса', "int_func('самса')"
assert int_func('') == '', "int_func('')"

assert user_temp('колбаса с сыром') == 'Колбаса С Сыром', "user_temp('колбаса с сыром')"
assert user_temp('самса с ветчиной') == 'Самса С Ветчиной', "user_temp('самса с ветчиной')"
assert user_temp('') == '', "user_temp('')"
