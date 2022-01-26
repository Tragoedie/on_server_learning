# Наследования вариаций (variation inheritance)
class Car:
    def run(self):
        print('It is usual car')


# Наследование функциональной вариацией (functional variation inheritance)
class Jeep(Car):
    def run(self):
        print('Beep, beep, i am Jeep')


# Наследование с вариацией типа (type variation inheritance)
class SportCar(Car):
    def run(self, label):
        print(f'{dope} is a sport car')


# Наследование с конкретизацией (reification inheritance)
class IAnimal:
    def make_sound(self, sound):
        pass


class CCat(IAnimal):
    def make_sound(self, sound):
        print(f'Cat says {sound}!')


class CDog(IAnimal):
    def make_sound(self, sound):
        print(f'Dog says {sound}!')


# Структурное наследование (structure inheritance)
class IncrementValue:
    def inc(self, obj):
        obj.value = obj.value + 1


class IntObject:
    def __init__(self, val):
        self.value = val
        self.increment = IncrementValue()

    def inc_val(self):
        self.increment.inc(self)