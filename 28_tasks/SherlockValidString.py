def SherlockValidString(s):
    s = list(s)
    change = True
    while change:
        change = False
        for x in range(len(s)-1):
            if s[x] > s[x+1]:
                s[x], s[x+1] = s[x+1], s[x]
                change = True
    work_massive = []
    while len(s) > 1:
        block = [s[0]]
        s.pop(0)
        change = True
        while change and len(s) > 0:
            change = False
            if block[0] == s[0]:
                block.append(s[0])
                s.pop(0)
                change = True
        work_massive.append(block)
    if len(s) != 0:
        work_massive.append(s)
    counter = -1
    if len(work_massive) == 1:
        return True
    elif len(work_massive) == 2:
        if len(work_massive[0]) == len(work_massive[1]):
            return True
        else:
            if len(work_massive[0]) > len(work_massive[1]):
                while len(work_massive[0]) > len(work_massive[1]):
                    work_massive[0].pop(0)
                    counter += 1
            else:
                while len(work_massive[0]) < len(work_massive[1]):
                    work_massive[1].pop(0)
                    counter += 1
    elif len(work_massive) > 2:
        change = True
        while change and counter < 2:
            change = False
            for i in range(len(work_massive)-2):
                if len(work_massive[i]) == len(work_massive[i+1]) and len(work_massive[i]) == len(work_massive[i+2]):
                    continue
                elif (len(work_massive[i]) != len(work_massive[i+1])) and len(work_massive[i+1]) == len(work_massive[i+2]):
                    if len(work_massive[i]) == 1:
                        work_massive.pop(i)
                    else:
                        work_massive[i].pop(0)
                    counter += 1
                    change = True
                    break
                elif (len(work_massive[i+1]) != len(work_massive[i])) and len(work_massive[i]) == len(work_massive[i+2]):
                    if len(work_massive[i+1]) == 1:
                        work_massive.pop(i+1)
                    else:
                        work_massive[i+1].pop(0)
                    counter += 1
                    change = True
                    break
                elif (len(work_massive[i+2]) != len(work_massive[i])) and len(work_massive[i]) == len(work_massive[i+1]):
                    if len(work_massive[i+2]) == 1:
                        work_massive.pop(i+2)
                    else:
                        work_massive[i+2].pop(0)
                    counter += 1
                    change = True
                    break
    if counter < 1:
        return True
    else:
        return False


# print(SherlockValidString('xyz'))
# print(SherlockValidString('xyzaa'))
# print(SherlockValidString('xxyyy'))
# print(SherlockValidString('xxxyy'))
# print(SherlockValidString('xyzzz'))
# print(SherlockValidString('xxyyza'))
# print(SherlockValidString('xxyyzabc'))
# print(SherlockValidString('xyxyzazaz'))

