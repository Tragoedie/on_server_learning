# Специализация:

class Ellipse:  # Класс «Эллипс»
    def __init__(self, Point, x, y):
        self.Center = Point  # Поля класса: центр и два радиуса.
        self.LowRadius = x  # меньший радиус.
        self.HighRadius = y  # больший радиус.

    def Draw(self):  # Методы класса: нарисовать эллипс
        ellipce = DrawEllipse(self.Center, self.LowRadius, self.HighRadius)

    def Move(self, NewPoint):
        self.Center = NewPoint  # передвинуть эллипс на плоскости


class Circle(Ellipse):  # Класс-наследник «Круг»
    def __init__(self, Point, x):  # Класс «Круг» поддерживает операции родительского класса «Эллипс»
        super().__init__(Point, x, x)

    def Draw(self):  # Но переопределяет реализацию методов
        circle = DrawCircle(self.Center, self.Radius)


# Расширение:

class Button:  # Класс «Кнопка»
    def __init__(self, id, caption, parent, window_styles, pushed):
        self.nID = id  # Поля класса: id
        self.CaptionText = caption  # Надпись на кнопке
        self.ParentWnd = parent  # Родительское окно
        self.Styles = window_styles  # Стили окна
        self.IsPushed = pushed  # Флаг нажатия


def PushButton(self):  # Метод класса: нажать кнопку
    self.IsPushed = not self.IsPushed


class ImageButton(Button):  # Расширенный класс кнопки

    def __init__(self, id, parent, window_styles, pushed, hBitmap):
        super().__init__(id, '', parent, window_styles, pushed)
        self.hBitmap = hBitmap  # Новое поле: объект bitmap

    def setImage(self, idBitmap):  # Новый метод: установка bitmap’а
        hBitmap = LoadBitmap(idBitmap)
