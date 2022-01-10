from typing import Generic, TypeVar


# Полиморфный вызов
class Parent:
    def __init__(self):
        pass

    def DoWork(self):
        print('I am working, do not worry, please!')


class Child(Parent):
    def DoHomework(self):
        print('I am doing homework!')


somebody = Child()
somebody.DoWork()

# Ковариантный вызов
car = TypeVar('Car', covariant=True)


class Car:
    def __init__(self):
        pass

    def signal(self):
        return None


class Jeep(Car):
    def signal(self):
        print('Beep, beep, i am Jeep!')


class Lada(Car):
    def signal(self):
        print('Lada is starting her trip!')
        print('Clap! Bams! Ouch!.. R.I.P.')


class Starter(Generic[car]):
    def __init__(self, object):
        self.__car_object = object

    def signal(self):
        self.__car_object.signal()


def start(starter_obj):
    starter_obj.signal()


car_obj = Lada()
starter = Starter(car_obj)
start(starter)
