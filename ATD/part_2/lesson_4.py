class Shape:                            # Абстрактный класс для наследования
    _central_point = {'x': 0, 'y': 0}   # protected член класса для наследования потомками

    def Draw(self):                     # public методы, доступные извне
        pass

    def Move(self, NewCentralPoint):
        self._central_point = NewCentralPoint
        self.Draw()


class Square(Shape):
    __edge = 0                          # private поле, означающее длину ребра квадрата

    def Draw(self):
        DrawSquare()


class Circle(Shape):
    __radius = 0                        # private поле, означающее радиус

    def Draw(self):
        DrawCircle()

# Для соблюдения принципа открытости-закрытости в языках программирования используются префиксы public,
# protected (_ in python) и private (__ in python). К публичным полям и методам возможно получить доступ извне,
# к приватным атрибутам доступ возможен только внутри методов класса, и они не наследуются, префикс protected
# аналогичен private, за исключением запрета на наследование поля/метода.
