def lenght(line):
    if len(line) == 1:
        return 1
    else:
        line.pop(0)
        return 1 + lenght(line)


# print(lenght(['1', '2', '3', '4', '5']))
# print(lenght(['1']))
