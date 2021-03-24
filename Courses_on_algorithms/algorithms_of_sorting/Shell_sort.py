import random


def InsertionSortStep(array, step, i):
    for j in range(i, len(array), step):
        key = array[j]
        h = j - step
        while h >= 0 and key < array[h]:
            array[h + step] = array[h]
            h -= step
        array[h + step] = key
    return array


def KnuthSequence(array_size):
    if array_size == 0:
        return [1]
    number = 1
    array = []
    while number <= array_size:
        array.append(number)
        number = 3 * number + 1
    array.reverse()
    return array


def Shell_sorting(array):
    step_for_sort = KnuthSequence(len(array))
    for i in range(len(step_for_sort)):
        step = step_for_sort[i]
        for j in range(step):
            InsertionSortStep(array, step, j)
    return array


arr = [9, 2, 5, 7, 8, 1, 13, 14, 11, 0, 3, 6, 4, 10, 12, 15]
print(Shell_sorting(arr))
arr_1 = []
print(Shell_sorting(arr_1))
arr_2 = [1]
print(Shell_sorting(arr_2))
arr_3 = [2, 1]
print(Shell_sorting(arr_3))
arr_4 = [i for i in range(1, 501)]
random.shuffle(arr_4)
print(arr_4)
print(Shell_sorting(arr_4))