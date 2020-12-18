"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""


def test_iter(*args):
    prev = float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num


if __name__ == '__main__':
    assert list(test_iter(1, 2, 3, 6, 5, 6, 7, 8)) == [2, 3, 6, 6, 7, 8]
    assert list(test_iter(-1, 3, 6, 12, -5, 0, 2, 7)) == [3, 6, 12, 0, 2, 7]
    assert list(test_iter(1)) == []

    test = [-1, 3, 6, 12, -5, 0, 2, 7]
    result = [itm for idx, itm in enumerate(test) if idx and itm > test[idx - 1]]
    print(result)
    assert result == [3, 6, 12, 0, 2, 7]
