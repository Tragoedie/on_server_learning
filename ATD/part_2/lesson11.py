from on_server_learning.ATD.part_2.lesson_9 import General, Any


# При помощи класса Void замкнули иерархию классов
class SomeClass(General):
    def __init__(self):
        pass


class Void(Any, SomeClass):
    def __new__(cls, *args, **kwargs):
        return None


x = Void()
if x is None:
    print('None object')


# Попытка наследования от класса Void
class InheritanceAttempt(Void):
    def print_val(self):
        print('val')


x = Void()
if x is None:
    print('None object')

# AttributeError: 'NoneType' object has no attribute 'print_val'
y = InheritanceAttempt()
y.print_val()
