def SumOfThe(N, data):
    count = 0
    data_work = data.copy()
    while count < N:
        summ = 0
        for j in range(1, N):
            summ += data_work[j]
        if data_work[0] == summ:
            return data_work[0]
        else:
            count += 1
            data_work[0], data_work[count] = data_work[count], data_work[0]
            #print(data_work)

#N = 4
#data = [100, -50, 10, -25, 90, -35, 90]
#data = [10, -25, -45, -35, 5]

#data = [10, 10, 0, 20]
#print(SumOfThe(N, data))
