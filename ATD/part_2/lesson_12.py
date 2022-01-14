from on_server_learning.ATD.part_2.lesson_9 import General
from on_server_learning.ATD.part_2.lesson_11 import Void


class GeneralEx(General):
    def __init__(self, int, str):
        self.int_field = int
        self.str_field = str
        self.array_field = []

    @classmethod
    def assignment_attempt(cls, target, source):
        if type(target) != cls or type(source) != cls:
            return Void()
        target.CopyFrom(source)
        return target


x = GeneralEx(10, 'x val')
y = GeneralEx(20, 'y val')
z = General()

x = GeneralEx.assignment_attempt(x, y)
print(x.int_field)
# 20
print(x.str_field)
# y val

x = GeneralEx.assignment_attempt(x, z)
# AttributeError: 'NoneType' object has no attribute 'int_field'
# print(x.int_field)
