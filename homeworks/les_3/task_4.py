# homework lesson: 3, task:4
"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

# x ** y = (x+x+x...(x раз)) + (x+x+x...(x раз)) ... y раз


from functools import reduce


def my_multip(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result


def my_func(x: float, y: int):
    result = 1
    for _ in range(abs(y)):
        result = my_multip(result, x)
    return result if y > 0 else 1 / result


def new_func(x, y):
    tmp_x = 0
    for _ in range(0, x):
        tmp_x += x
    tmp_result = 0
    for _ in range(0, y - 1):
        tmp_result += tmp_x
    print(1)


# Немного програйминг извращений
# никогда так не делайте lambda созданы не для этого это читается ужасно, и вообще зачем?
my_func2 = lambda x, y: reduce(
    lambda a, b: a * b, [x for _ in range(abs(y))] or [1]
) if y > 0 else 1 / reduce(
    lambda a, b: a * b, [x for _ in range(abs(y))] or [1])

if __name__ == '__main__':
    print(my_func(0, -2))
    # assert my_func(1.5, 2) == 1.5 ** 2, 'my_func(2, 2)'
    # assert my_func(3, 3) == 3 ** 3, 'my_func(3, 3)'
    # assert my_func(3, -5) == 3 ** -5, 'my_func(3, -5)'
    # assert my_func(3, 0) == 3 ** 0, 'my_func(3, 0)'
    #
    # assert my_func2(2, 2) == 2 ** 2, 'my_func2(2, 2)'
    # assert my_func2(3, 3) == 3 ** 3, 'my_func2(3, 3)'
    # assert my_func2(3, -5) == 3 ** -5, 'my_func2(3, -5)'
    # assert my_func2(3, 0) == 3 ** 0, 'my_func2(3, 0)'
    #
    # print(my_func(2, 2))
