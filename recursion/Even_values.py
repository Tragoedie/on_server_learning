def even_values(list, i=0):
    if list[i] % 2 == 0:
        print(list[i])
    if i + 1 < len(list):
        even_values(list, i + 1)


# even_values([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
