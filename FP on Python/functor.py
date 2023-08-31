"""
Задание.
Ещё одна мощная фишка функторов -- это возможность использования их в отложенном применении.
На основе функции add() сделайте функцию add10() с одним Just-аргументом,
которая прибавляет 10 к Just- или List-аргументу.
"""
from pymonad import Just, List, Nothing, curry


@curry
def add(x, y):
    return x + y


# 1
add10 = add(10)

'''
# 2
@curry
def add10(x):
    return x + 10
'''

print(add10 * Just(7))
print(add10 * List(1, 2))
print(List(1, 2, 3).fmap(add10))
