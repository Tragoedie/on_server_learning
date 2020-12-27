def PatternUnlock(N, hits):
    s_line = 0
    for i in range(N-1):
        if hits[i] == 2 and (hits[i+1] == 9 or hits[i+1] == 7 or hits[i+1] == 4 or hits[i+1] == 6):
            s_line += pow(2, 0.5)
            continue
        if hits[i] == 2 and (hits[i+1] == 1 or hits[i+1] == 8 or hits[i+1] == 3 or hits[i+1] == 5):
            s_line += 1
            continue
        if (hits[i] == 6 or hits[i] == 9 or hits[i] == 7 or hits[i] == 4) and hits[i+1] == 2:
            s_line += pow(2, 0.5)
            continue
        if (hits[i] == 6 or hits[i] == 9 or hits[i] == 7 or hits[i] == 4) and (hits[i+1] == 1 or hits[i+1] == 8 or hits[i+1] == 3 or hits[i+1] == 5):
            s_line += 1
            continue
        if (hits[i] == 1 or hits[i] == 8 or hits[i] == 3 or hits[i] == 5) and hits[i+1] == 2:
            s_line += 1
            continue
        if (hits[i] == 1 or hits[i] == 8 or hits[i] == 3 or hits[i] == 5) and (hits[i+1] == 6 or hits[i+1] == 9 or hits[i+1] == 7 or hits[i+1] == 4):
            s_line += 1
            continue
    # print(s_line)
    s_line = round(s_line, 5)
    # print(s_line)
    code = str(s_line)
    code = list(code)
    # print(code)
    x = 0
    while x < len(code):
        if code[x] == '.' or code[x] == '0':
            code.pop(x)
        else:
            x += 1
    code = ''.join(code)
    return code
    # print(code)


# hits = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
# N = 10
# PatternUnlock(N, hits)
