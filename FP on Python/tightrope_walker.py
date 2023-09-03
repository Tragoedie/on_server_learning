"""
Некий канатоходец ходит по канату с шестом, но на шест любят садиться птицы, а потом могут и улететь.
Канатоходец может держать равновесие, если разность кол-ва птиц на сторонах шеста не более 4.
Ну и канатоходец просто может упасть подскользнувшись на банановой кожуре.
Нужно смоделировать симуляцию последовательности событий с выдачей результата в виде "упал" / "не упал".

# Код:
# посадка птиц на левую сторону
to_left = lambda num: lambda (l, r): (
    nothing()
    if abs((l + num) - r) > 4
    else just((l + num, r))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda (l, r): (
    nothing()
    if abs((r + num) - l) > 4
    else just((l, r + num))
)

# банановая кожура
banana = lambda x: nothing()

# отображение результата
def show(maybe):
    falled, pole = maybe.result
    print not falled

# начальное состояние
begin = lambda: just( (0,0) )

show(
    begin()
    +'>>='+ to_left(2)
    +'>>='+ to_right(5)
    +'>>='+ to_left(-2) # канатоходец упадёт тут
)
show(
    begin()
    +'>>='+ to_left(2)
    +'>>='+ to_right(5)
    +'>>='+ to_left(-1)
) # в данном случае всё ок
show(
    begin()
    +'>>='+ to_left(2)
    +'>>='+ banana # кожура всё испортит
    +'>>='+ to_right(5)
    +'>>='+ to_left(-1)
)


В статье есть вторая задача про канатоходца, тоже по сути в декларативном стиле. Перепишите её на работу с PyMonad.
Обратите внимание, что, во-первых, поле .result (извлечение данных из функтора) в оригинальном примере 
надо заменить на метод getValue(), и во-вторых, в функции вывода результата show() случай, когда канатоходец упал, 
выявляется простой проверкой параметра maybe на равенство Nothing. Если канатоходец держится нормально, 
то результат будет представлен в виде функтора Just(), который обёртывает список из двух элементов 
(сколько птиц слева и сколько птиц справа).
"""

# Код:
from pymonad import Just, Maybe, Nothing

# посадка птиц на левую сторону
to_left = lambda num: lambda pos: (
    Nothing
    if abs((pos[0] + num) - pos[1]) > 4
    else Just((pos[0] + num, pos[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda pos: (
    Nothing
    if abs((pos[1] + num) - pos[0]) > 4
    else Just((pos[0], pos[1] + num))
)

# банановая кожура
banana = lambda x: Nothing


# отображение результата
def show(maybe):
    if maybe != Nothing:
        print(maybe.getValue())
    else:
        print(False)


# начальное состояние
begin = lambda: Just((0, 0))

show(begin() >> to_left(2) >> to_right(5) >> to_left(-2))
show(begin() >> to_left(2) >> to_right(5) >> to_left(-1))
show(begin() >> to_left(2) >> banana >> to_right(5) >> to_left(-1))