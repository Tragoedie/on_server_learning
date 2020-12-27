def UFO(N, data, octal):
    work_massive = []
    for i in range(N):
        work_sum = 0
        number = data[i]
        exponent = 0
        while number > 0:
            work_number = number % 10
            if octal is True:
                work_number = (work_number * pow(8, exponent))
            else:
                work_number = (work_number * pow(16, exponent))
            work_sum += work_number
            number = number // 10
            exponent += 1
        work_massive.append(work_sum)
    return work_massive


# N = 2
# data = [1234, 1777]
# octal = False
# print(UFO(N, data, octal))
