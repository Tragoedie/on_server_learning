"""
Задание.

Реализуйте вышеописанный пример с покупками с помощью монад состояний.
У нас есть условный покупатель (корзина покупок и денежный счет):

user = {"items":[],"money":2000}
Есть перечень продуктов в магазине:

items = {"apples":70,
         "wine":300,
         "milk":80,
         "chips":100
}
Напишите функцию buy, которая выполняет нужные операции с покупателем и возвращает условный
результат покупок (покупатель и общая сумма покупок).
Учтите ситуацию, когда на счету может не хватить денег, или когда задан отсутствующий товар.
"""
from pymonad import curry, unit, State


user = {"items": {}, "money": 2000}

items = {
    "apples": 70,
    "wine": 300,
    "milk": 80,
    "chips": 100,
}


@curry
def buy(item, customer):
    @State
    def buy_item(old_state):
        if item not in items.keys():
            print(item, "out of stock")
            return customer, old_state
        if (customer["money"]) - items[item] < 0:
            print("not enough money to buy", item)
            return customer, old_state
        if item not in customer["items"].keys():
            customer["items"][item] = 1
        else:
            customer["items"][item] = customer["items"][item] + 1
        customer["money"] = customer["money"] - items[item]
        return customer, old_state + items[item]
    return buy_item


x = unit(State, user) >> buy("apples") >> buy("apples") >> buy("wine") >> buy("chips") >> buy("wine") \
    >> buy("milk") >> buy("milk") >> buy("chips") >> buy("bread") >> buy("chips") >> buy("wine") \
    >> buy("milk") >> buy("milk") >> buy("chips") >> buy("watermellon") >> buy("chips") >> buy("wine")
print(x(0))
