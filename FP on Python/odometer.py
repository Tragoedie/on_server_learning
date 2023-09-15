from functools import reduce


def odometer(oksana):
    if len(oksana) < 2:
        raise Exception("Sorry, wrong data")
    return reduce(
        lambda a, b: a + b, list(
            map(lambda x, y: x * y, oksana[0:len(oksana):2], (
                    [oksana[1]] + list(map(lambda x, y: y - x, oksana[1::2], oksana[3::2]))
            ))
        )
    )


data = [15, 1, 25, 2, 30, 3, 10, 5]
print(odometer(data))  # 90
data_2 = [10, 1, 20, 2]
print(odometer(data_2))  # 30
data_3 = [30, 1]
print(odometer(data_3))  # 30
data_4 = [0]
print(odometer(data_4))
