class VinCodeError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def vin_validator(cls, vincode):
        if not isinstance(vincode, str):
            raise cls('Тип винкода должен быть строчным')
        elif len(vincode) < 10:
            raise cls('Длина винкода не соответсвует правилу')
        return vincode


class Car:
    def __init__(self, name, vincode):
        self.name = name
        self.vincode = VinCodeError.vin_validator(vincode)


if __name__ == '__main__':
    try:
        car1 = Car('NAME', '12')
    except VinCodeError:
        print('надо создать другую машину')
        car1 = Car('NAME', 'fjgfgfgfjfgjhfgjfgjwhiusishuhsius')
    print(1)
    
