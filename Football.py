def Football(F, N):
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    if change:
        return True
    index_x = -1
    index_y = -1
    counter = 0
    for x in range(len(F)-1):
        if F[x] > F[x+1]:
            if index_x == -1:
                index_x = x
                index_y = x+1
                counter += 1
            else:
                index_y = x + 1
                counter += 1
    if counter < 3 and index_x != -1 and index_y != -1:
        F[index_x], F[index_y] = F[index_y], F[index_x]
        counter = -1
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    if change:
        return True
    else:
        if counter == -1:
            F[index_x], F[index_y] = F[index_y], F[index_x]
    if change is False:
        if index_x == 0:
            line_F = (index_y - (index_x)) // 2
        else:
            line_F = (index_y - (index_x - 1)) // 2
        for i in range(index_x, index_y + 1):
            if i <= line_F:
                F[i], F[index_y + index_x - i] = F[index_y - index_x - i], F[i]
    change = True
    for i in range(N-1):
        if F[i] > F[i+1]:
            change = False
    return change


# print(Football([5, 2, 3, 4, 1], 5))
# print(Football([1, 3, 2, 4, 5], 5))
# print(Football([1, 4, 3, 2, 5], 5))
# print(Football([1, 7, 5, 3, 9], 5))
# print(Football([1, 7, 6, 5, 4, 3, 2, 8], 8))
# print(Football([1, 7, 6, 5, 4, 3, 2], 7))
# print(Football([7, 6, 5, 4, 3, 2, 8], 7))
# print(Football([7, 6, 5, 4, 3, 2], 6))
# print(Football([9, 5, 3, 7, 1], 5))
