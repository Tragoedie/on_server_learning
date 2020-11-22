def after_max(list, i=0, max_1=0, max_2=0):
    if list[i] > max_1:
        if max_2 < max_1:
            max_2 = max_1
        max_1 = list[i]
    if i + 1 < len(list):
        return after_max(list, i+1, max_1, max_2)
    else:
        return max_2


print(after_max([1, 1, 8, 9, 7, 8, 9, 10]))