# homework lesson: 6, task:1

"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния
(красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time
from itertools import cycle


class TrafficLight:
    __modes = (("red", 7), ("yellow", 2), ("green", 5), ("yellow", 2))
    __light_start = 0
    __next_light = 0
    
    def __init__(self):
        self.__color = self.__modes[0][0]
        self.__light_start = time.time()
        self.__tic()
    
    def running(self):
        """
        Основной цикл проверяет поменялся-ли цвет, и выводит его на экран.
        :return: None
        """
        prew_color = None
        while True:
            self.__tic()
            if prew_color != self.__color:
                prew_color = self.__color
                print(self.__color)
    
    def __tic(self):
        """
        В зависимости от прошедшего времени переключаем цвет светофора.
        При этом не предполагается использование блокировки sleep.
        :return: str
        """
        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color, self.__light_start = (self.__modes[self.__next_light][0],
                                                time.time(),)
            self.__next_light = (
                self.__next_light + 1
                if len(self.__modes) > self.__next_light + 1
                else 0
            )
    
    def color(self):
        self.__tic()
        return self.__color
    
    def set_mode(self, color):
        if self.__modes[self.__next_light][0] != color:
            raise ValueError("Неможно включить этот цвет")
        self.__tic()


if __name__ == "__main__":
    lighter = TrafficLight()
    time.sleep(0.5)
    lighter2 = TrafficLight()
    time.sleep(0.5)
    lighter3 = TrafficLight()
    time.sleep(0.5)
    for light in cycle((lighter, lighter2, lighter3)):
        print(light.color())
        time.sleep(1)