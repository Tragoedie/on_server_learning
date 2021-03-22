def SelectionSortStep(array, i):
    if i + 1 >= len(array):
        return array
    min_number_index = array.index(min(array[i + 1:]))
    array[i], array[min_number_index] = array[min_number_index], array[i]
    return array


def BubbleSortStep(array):
    xchange = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            xchange = False
    return xchange


def InsertionSortStep(array, step, i):
    for j in range(i, len(array), step):
        key = array[j]
        h = j - step
        while h >= 0 and key < array[h]:
            array[h + step] = array[h]
            h -= step
        array[h + step] = key
    return array

