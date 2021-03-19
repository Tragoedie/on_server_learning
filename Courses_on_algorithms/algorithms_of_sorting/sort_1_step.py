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

