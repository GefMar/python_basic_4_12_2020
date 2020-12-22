import random


class Car:
    population = []
    
    def __init__(self, color, year, brand, model):
        self.color = color
        self.year = year
        self.brand = brand
        self.model = model
        self.population.append(self)
    
    def run(self):
        print('DRDRDR')


class Wolf:
    _some_protected = 'Protected'
    __some_private = 'PRIVATE'
    
    def __init__(self, color, height, sex):
        self.color = color
        self.height = height
        self.sex = sex
    
    def say(self):
        print('RRRRRRRRRRAAAAYYYYYYYYYYYYYYYYY')


class Dog(Wolf):
    
    def __init__(self, name, color, height):
        super().__init__(color, height, random.choice(('f', 'm')))
        self.name = name
    
    def say(self):
        print('WOFFFF')
    
    def tic(self):
        print(self._Wolf__some_private)
