# Используя наследование реализации, создаём иерархию классов, эмулирующих тип протагониста
# (Кочевник, Корпорат или Дитя улиц) из игры Cyperpunk 2077.
class ProtagonistType:
    def self_presentation(self):
        pass


class Nomad(ProtagonistType):
    def self_presentation(self):
        print('I\'m Nomad, i like fast driving and doing "Beep-beep"!')


class Corpo(ProtagonistType):
    def self_presentation(self):
        print('I\'m Corpo, i like sound of money rustle and smell of new banknotes!')


class StreetKid(ProtagonistType):
    def self_presentation(self):
        print('I\'m Street Kid, peef-puff, you are dead!')


# Основной класс Протагонист, который включает тип как атрибут
class Protagonist():
    def __init__(self, type):
        self.type = type
