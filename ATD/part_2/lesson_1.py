# Наследование

class Parent:  # Родительский класс
    def __init__(self):
        self.field1 = 1  # Поля родительского класса
        self.field2 = 2


class Child(Parent):  # Класс-наследник
    def __init__(self):
        super().__init__()

    def function_for_child(self):  # ф-ция, использующая поля родительского класса
        return self.field1 + self.field2


# Композиция

class Node:  # Класс – элемент списка
    def __init__(self, val):
        self.value = val
        self.next = None  # Объект Node, указатель на следующий элемент


class List:  # Класс списка
    def __init__(self):
        self.head = None  # «Голова» и «хвост» списка
        self.tail = None

    def addVal(self, val):
        item = Node(val)  # класс List, содержит объекты класса Node
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            self.tail = item


# Полиморфизм:

class foo:  # Класс foo с методом info()
    def info(self):
        print("foo")


class bar:  # Класс bar с методом info()
    def info(self):
        print("bar")


f = foo()  # Создаём объект класса foo
b = bar()  # Создаём объект класса bar

for obj in (f, b):  # упаковываем объекты в кортеж
    obj.info()  # и можем итерировать по нему
