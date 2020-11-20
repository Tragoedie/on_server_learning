def lenght(line):
    if line == []:
        return 0
    else:
        line.pop(0)
        return 1 + lenght(line)


print(lenght(['1', '2', '3', '4', '5']))
print(lenght(['1']))
print(lenght([]))
