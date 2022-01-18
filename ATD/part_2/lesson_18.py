"""
Пример 1: Транспортное средство -> Автомобиль и др.
Базовым классом будет транспортное средство с набором единных для всех транспортных средств методов: move(), accel(),
brake(), turn_left(), turn_right() и др. Все остальные производные классы (автомобиль, мотоцикл, поезд, корабль и др)
дополняют данный набор методов своими сосбтвенными методами, специфичными для данного средства передвижения.

Пример 2: Игровой персонаж -> NPC.
Базовым классом будет игровой персонаж, который будет расширен классами Герой (аватар игрока) и NPC (non-playable
character - неигровой персонаж, управляемый ИИ). Общими будут методы передвижения, физической атаки, анимации речи и пр.
Для классов-наследников этот список будет расширяться, например, анимации социального взаимодействия (приветствие, танец
и пр.), поднятие уровня, смена класса, изучение умений и навыков и пр. Для NPC это расчёт поведенческие скрипты, возрож-
дение после смерти и пр.
"""