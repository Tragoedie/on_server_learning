def WordSearch(ilen, s, subs):
    line = list(s)
    work_line = []
    work_massive = []
    while len(line) > ilen:
        xchange = 0
        for i in range(ilen, 0, -1):
            if line[i] == ' ':
                xchange = 1
                for j in range(0, i + 1):
                    work_line.append(line[0])
                    line.pop(0)
                work_line = ''.join(work_line)
                work_massive.append(work_line)
                work_line = []
                break
        if xchange == 0:
            for j in range(0, ilen):
                work_line.append(line[0])
                line.pop(0)
            work_line = ''.join(work_line)
            work_massive.append(work_line)
            work_line = []
    line = ''.join(line)
    work_massive.append(line)
    #print(work_massive)
    line_outcome = []
    for x in range(len(work_massive)):
        if len(work_massive[x]) == len(subs):
            count = True
            for y in range(len(subs)):
                if subs[y] != work_massive[x][y]:
                    count = False
                    line_outcome.append(0)
                    break
            if count is True:
                line_outcome.append(1)
        else:
            count = False
            for y in range(len(work_massive[x])-len(subs)+1):
                count = True
                for z in range(len(subs)):
                    if subs[z] != work_massive[x][z + y]:
                        count = False
                        break
                if count is False:
                    continue
                index_begin = y
                index_end = z + y
                if index_begin != 0:
                    if work_massive[x][index_begin - 1] != ' ':
                        count = False
                        continue
                if index_end < (len(work_massive[x])-1):
                    if work_massive[x][index_end + 1] != ' ':
                        count = False
                        continue
                break
            if count == True:
                line_outcome.append(1)
            else:
                line_outcome.append(0)
    return line_outcome
    #print(line_outcome)


#ilen = 5
#s = 'строкпо разбивается на набор строк через выравнивание строкпо заданной ширине'
#subs = 'строк'
#print(WordSearch(ilen, s, subs))
