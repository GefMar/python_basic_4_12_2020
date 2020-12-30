# homework lesson: 7, task:2

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def consumption(self) -> float:
        pass

    @property
    @abstractmethod
    def params(self) -> float:
        pass


class Suit(Wear):

    def __init__(self, name: str, height: float):
        self.__height = height
        self.name = name

    @property
    def consumption(self) -> float:
        return 2 * self.__height + 0.3

    @property
    def params(self) -> float:
        return self.__height


class Coat(Wear):
    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def consumption(self) -> float:
        return self.__size / 6.5 + 0.5

    # @property
    # def params(self) -> float:
    #     return self.__size


if __name__ == '__main__':
    suit = Suit('Костюм', 175)
    coat = Coat('Пальто', 48)
    print(1)
