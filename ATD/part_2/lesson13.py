# В Python существует формальный метод задания модификаторов доступа protected и private при помощи _ и __
# соответственно, только соблюдение правильности доступа ложится на плечи разрабочиков. При помощи библиотеки
# accessify возможна реализация модификаторов доступа как и в других языках программирования, т.е. контроль за
# осуществление проверку доступа ложится на интерпретатор.
# Варианты 1 и 4.

from accessify import protected


class Car:
    def __init__(self):
        pass

    @private
    def start_engine(self):
        return "Engine's sound."

    def run(self):
        return self.start_engine()


if __name__ == '__main__':
    car = Car()

    assert "Engine's sound." == car.run()

    car.start_engine()

'''
Traceback (most recent call last):
  File "examples/access/private.py", line 24, in <module>
    car.start_engine()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/accessify/main.py", line 92, in private_wrapper
    class_name=instance_class.__name__, method_name=method.__name__,
accessify.errors.InaccessibleDueToItsProtectionLevelException: Car.start_engine() is inaccessible due to its protection level
'''