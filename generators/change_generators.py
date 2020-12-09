def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum)
        if x < n - 1:
            yield
        else:
            yield sum


def long_process_generator(massive):
    max_number = massive[0]
    for i in range(len(massive)):
        if massive[i] > max_number:
            max_number = massive[i]
    R = {}
    R_total = {}
    for j in range(len(massive)):
        id_number = 'Id' + str(j + 1)
        Id = long_process(id_number, massive[j])
        R[id_number] = Id
        R_total[id_number] = None
    for y in range(max_number):
        for x in range(len(R)):
            id_number = 'Id' + str(x + 1)
            if R_total[id_number] is None: R_total[id_number] = next(R[id_number])
    return R_total


print(long_process_generator([10, 100, 256, 120, 3, 8]))
