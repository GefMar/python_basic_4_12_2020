from typing import List

some_list = [1, 2, 3, [11, 21, 31, [22, 33]], 1, 1, [[[44, 45]]]]

result = [1, 2, 3, 11, 21, 31, 22, 33, 1, 1, 44, 45]


def flat_list(data: List[list]) -> List[int]:
    for itm in data:
        if isinstance(itm, list):
            yield from flat_list(itm)
        else:
            yield itm
    return result


some_result = list(flat_list(some_list))
print(1)
