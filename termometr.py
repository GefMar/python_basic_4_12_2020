class Temperature:
    __KELVIN_CONST_C = 273.15
    __slots__ = ('kelvin',)

    def __init__(self):
        self.kelvin = 0
        # self.new_cell = 222

    @property
    def celsius(self):
        return self.kelvin - self.__KELVIN_CONST_C

    @celsius.setter
    def celsius(self, temperature):
        self.kelvin = temperature + self.__KELVIN_CONST_C

if __name__ == '__main__':
    temp = Temperature()
    print(1)
