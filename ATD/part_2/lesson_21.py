# Наследование реализации (implementation inheritance)
class GridButtonCell:
    def __init__(self, image):
        self.btn_image = image

    def OnClick(self):
        self.SetFocus()


class GridCheckBoxCell(GridButtonCell):
    def __init__(self, image, bIsChecked):
        super.__init__(image)
        self.bIsChecked = bIsChecked

    def OnClick(self):
        self.bIsChecked = not self.bIsChecked
        self.DrawButton()
        super().OnClick()


# Льготное наследование (facility inheritance)
class Animal:
    sound = 'Here can be your advertising!'

    def make_sound(self):
        print(self.sound)


class Cat(Animal):
    sound = 'Meow-meow'


class Dog(Animal):
    sound = 'Woof-woof'
