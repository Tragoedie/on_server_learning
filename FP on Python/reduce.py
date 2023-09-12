from functools import reduce


# first
def find2max(array: list):
    if array.__len__() < 2:
        return None
    maxy = reduce((lambda x, y: x if x > y else y), array)
    if array.count(maxy) > 1:
        return maxy
    return reduce((lambda x, y: x if y < x < maxy or y == maxy else y), array)


arr = [1, 2, 3, 4, 5]  # 4
print(find2max(arr))
arr = [1, 2, 3, 4, 4]  # 4
print(find2max(arr))


# second
def find2max_2(array: list):
    if array.__len__() < 2:
        return None
    maxy, second_maxy = reduce(
        lambda x, y: (y if y >= x[0] else x[0], y if x[0] >= y > x[1] else x[0] if y > x[0] else x[1]), array[2:],
        (array[0], array[1]) if array[0] > array[1] else (array[1], array[0])
    )
    return second_maxy


array_1 = [1, 2, 3, 4, 4]  # 4
print(find2max_2(array_1))
array_2 = [1, 2, 3, 4, 5]  # 4
print(find2max_2(array_2))
array_3 = [5, 4, 3, 2, 1]  # 4
print(find2max_2(array_3))
array_4 = [4, 4, 3, 2, 1]  # 4
print(find2max_2(array_4))
array_5 = [0]  # None
print(find2max_2(array_5))
array_6 = [0, 1]  # 0
print(find2max_2(array_6))
array_7 = [4, 4, 4, 4, 4]  # 4
print(find2max_2(array_7))
