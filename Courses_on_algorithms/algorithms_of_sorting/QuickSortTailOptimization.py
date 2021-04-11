def ArrayChunk(M, left, right):
    i_1 = left
    i_2 = right
    index_N = (right - left + 1) // 2 + left
    N = M[index_N]
    while True:
        while M[i_1] < N:
            i_1 += 1
        while M[i_2] > N:
            i_2 -= 1
        if i_1 == i_2 - 1 and M[i_1] > M[i_2]:
            M[i_1], M[i_2] = M[i_2], M[i_1]
            index_N = (right - left + 1) // 2 + left
            N = M[index_N]
            i_1 = 0
            i_2 = len(M) - 1
            continue
        if i_1 == i_2 or (i_1 == (i_2 - 1) and M[i_1] < M[i_2]):
            return index_N
        M[i_1], M[i_2] = M[i_2], M[i_1]
        if M[i_1] == N:
            index_N = i_1
        elif M[i_2] == N:
            index_N = i_2


def QuickSortTailOptimization(array, left, right):
    while left < right:
        index = ArrayChunk(array, left, right)
        QuickSortTailOptimization(array, left, index - 1)
        left = index + 1

