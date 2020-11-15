def BiggerGreater(input):
    input = list(input)
    index_j = -1
    index_i = -1
    for i in range(len(input)-2, -1, -1):
        for j in range(i + 1, len(input)):
            if (input[i] < input[j] and index_j == -1) or (input[i] < input[j] and input[j] < input[index_j]):
                index_j = j
                index_i = i
        if index_j != -1:
            input[index_i], input[index_j] = input[index_j], input[index_i]
            break
    if index_j != -1:
        change = True
        while change:
            change = False
            for x in range(index_i + 1, len(input) - 1):
                if input[x] > input[x+1]:
                    input[x], input[x+1] = input[x+1], input[x]
                    change = True
    if index_j == -1:
        return ''
    else:
        input = ''.join(input)
        return input


# print(BiggerGreater('ая'))
# print(BiggerGreater('fff'))
# print(BiggerGreater('нклм'))
# print(BiggerGreater('вибк'))
# print(BiggerGreater('вкиб'))
