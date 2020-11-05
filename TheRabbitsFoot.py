def TheRabbitsFoot(s, encode):
    line = list(s)
    if encode is True:
        i = 0
        while i < len(line):
            if line[i] == ' ':
                line.pop(i)
            else:
                i += 1
        # print(line)
        line_size = int(pow(len(line), 0.5))
        column_size = line_size + 1
        if line_size * column_size < len(line):
            line_size += 1
        # print(line_size)
        # print(column_size)
        work_line = []
        for x in range(line_size-1):
            work_line_2 = []
            for y in range(column_size):
                work_line_2.append(line[0])
                line.pop(0)
            work_line.append(work_line_2)
        if len(line) > 0:
            work_line.append(line)
        # print(work_line)
        work_line_2 = []
        for j in range(column_size):
            b = []
            for z in range(len(work_line)):
                if j < (len(work_line[z])):
                    b.append(work_line[z][j])
            b.append(' ')
            work_line_2.append(b)
        work_line_2[len(work_line_2)-1].pop(len(work_line_2[len(work_line_2)-1])-1)
        # print(work_line_2)
        for i in range(len(work_line_2)):
            work_line_2[i] = ''.join(work_line_2[i])
        work_line_2 = ''.join(work_line_2)
        # print(work_line_2)
        return work_line_2
    if encode is False:
        b = []
        work_line = []
        for i in range(len(line)):
            if line[i] != ' ':
                b.append(line[i])
            else:
                if b:
                    work_line.append(b)
                    b = []
        if b:
            work_line.append(b)
        # print(work_line)
        work_line_2 = []
        for j in range(len(work_line[0])):
            b = []
            for z in range(len(work_line)):
                if j < (len(work_line[z])):
                    b.append(work_line[z][j])
            b = ''.join(b)
            work_line_2.append(b)
        work_line_2 = ''.join(work_line_2)
        # print(work_line_2)
        return work_line_2

# s = 'отдай мою кроличью лапкy'
# s = ' омоюy толл дюиа акчп йрьк '
# encode = True
# encode = False
# print(TheRabbitsFoot(s, encode))
