# homework lesson: 2, task:2

"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_answer = input('введите список через запятую')
user_list = user_answer.split(',')

idx = 0
len_list = len(user_list) - 1
while idx < len_list:
    user_list[idx], user_list[idx + 1] = user_list[idx + 1], user_list[idx]
    idx += 2
print(user_list)
