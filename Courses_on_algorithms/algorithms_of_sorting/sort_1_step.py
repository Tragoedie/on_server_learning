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


def ArrayChunk(M):
    if len(M) <= 1:
        return 0
    N = len(M) // 2
    i_1 = 0
    i_2 = len(M) - 1
    while True:
        while M[i_1] < N:
            i_1 += 1
        while M[i_2] > N:
            i_2 -= 1
        if i_1 == i_2 or (i_1 == (i_2 - 1) and M[i_1] < M[i_2]):
            return N
        M[i_1], M[i_2] = M[i_2], M[i_1]

