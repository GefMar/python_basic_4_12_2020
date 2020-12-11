"""DRY"""
"""
Необходимо напечатать на экране YES, NO если переданное число (ЦЕЛОЕ) имеет 3 цифры
"""


def is_some(number: int, count: int) -> bool:
    """ Функция возвращает является ли число n разрядным
    :param number: int: Число
    :param count: int: Количество цифр в числе
    :return: bool
    """
    return 1 <= (number // 10 ** (count - 1)) < 10


#
#
#
#
# a = {
#     'count': 5,
#     'number': 23456,
# }
# c = dict(count=3, number=3)
# b = [23456, 5]
#
# print(is_some(*b))

def my_map(funk, iter_obj):
    for item in iter_obj:
        yield funk(item)


def my_sum(*args, **kwargs):
    print('kwargs', kwargs)
    print(args)
    result = 0
    for n in args:
        result += n
    return result


# print(my_sum(1, 2, 3, 4, 5, 6, 7, 10, 123, factor=2))

a = 1
b = 10

c = []

for n in range(a, b + 1):
    c.append(n ** 2)
print(c)

d = [n ** 2 for n in range(a, b + 1)]
print(d)

nums_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
nums_b = [100, 200, 300, 400, 500]

# nums_combinations = [(n_a, n_b) for n_a in nums_a for n_b in nums_b]

# result = {1: 1 ** 2, 2: 2**2}

nums_result = tuple(n for n in nums_a if not n & 1)

print(nums_result)

# result = []
# for n_a in nums_a:
#     for n_b in nums_b:
#         result.append((n_a, n_b))
# print(nums_combinations)
"""
zip
map
reduce
filter
enumerate
range
sum
min
max
len

"""
