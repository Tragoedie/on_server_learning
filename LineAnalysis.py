def LineAnalysis(line):
    line = list(line)
    if line[0] != '*':
        return False
    if len(line) == 1:
        return True
    pattern = []
    work_line = []
    for i in range(1, len(line)):
        pattern.append(line[i])
        if line[i] == '*':
            break
    if len(pattern) == 1:
        for x in range(len(line)):
            if line[i] != pattern[0]:
                return False
        return True
    pattern_l = []
    for j in range(1, len(line)):
        pattern_l.append(line[j])
        if line[j] == '*':
            work_line.append(pattern_l)
            pattern_l = []
    xchange = True
    for a in range(len(work_line)):
        for b in range(len(work_line[0])):
            if work_line[a][b] != pattern[b]:
                xchange = False
                break
    return xchange
    print(work_line)
    print(pattern)

# line = '*.......*.......*'
# line = '*..*..*..**..*..*..*'
# print(LineAnalysis(line))
