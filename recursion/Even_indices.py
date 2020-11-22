def even_indices(list, i=0):
    print(list[i])
    if i + 2 < len(list):
        even_indices(list, i+2)


even_indices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_indices(['a', 'b', 'c', 'd', 'e'])
