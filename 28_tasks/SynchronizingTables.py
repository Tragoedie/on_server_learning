def SynchronizingTables(N, ids, salary):
    ids_copy = ids.copy()
    salary_copy = salary.copy()
    x_change = True
    while x_change:
        x_change = False
        for i in range(N - 1):
            if ids_copy[i] > ids_copy[i + 1]:
                ids_copy[i], ids_copy[i + 1] = ids_copy[i + 1], ids_copy[i]
                x_change = True
    y_change = True
    while y_change:
        y_change = False
        for j in range(N - 1):
            if salary_copy[j] > salary_copy[j + 1]:
                salary_copy[j], salary_copy[j + 1] = salary_copy[j + 1], salary_copy[j]
                y_change = True
    for x in range(N):
        for y in range(N):
            if ids_copy[x] == ids[y]:
                salary[y] = salary_copy[x]
    return salary


    # print(ids)
    # print(ids_copy)
    # print(salary)
    # print(salary_copy)

# N = 5
# ids = [50, 1, 1024, 508, 705]
# salary = [45000, 100000, 100000, 45000, 70000]
# SynchronizingTables(N, ids, salary)