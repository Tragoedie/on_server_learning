def SetMinMax(first_num, second_num, max_num, min_num):
    list_1 = list(first_num)
    list_2 = list(second_num)
    if len(list_1) > len(list_2):
        max_num = list_1
        min_num = list_2
    elif len(list_2) > len(list_1):
        max_num = list_2
        min_num = list_1
    else:
        max_num = list_1
        min_num = list_2
        for j in range(len(list_1)):
            if int(list_2[j]) > int(list_1[j]):
                max_num = list_2
                min_num = list_1
                break

def BigMinus(s1, s2):
    max_number = []
    min_number = []
    SetMinMax(s1, s2, max_number, min_number)
    difference = []
    xchange = False
    for i in range(0, len(min_number)):
        if int(max_number[len(max_number) - 1 - i]) >= int(min_number[len(min_number) - 1 - i]):
            if xchange is False:
                number = int(max_number[len(max_number) - 1 - i]) - int(min_number[len(min_number) - 1 - i])
                difference.append(number)
            else:
                number = int(max_number[len(max_number) - 1 - i]) - int(min_number[len(min_number) - 1 - i]) - 1
                if number < 0:
                    number = (10 + int(max_number[len(max_number) - 1 - i])) - int(min_number[len(min_number) - 1 - i]) - 1
                    difference.append(number)
                else:
                    difference.append(number)
                    xchange = False
        else:
            if xchange is False:
                number = 10 + int(max_number[len(max_number) - 1 - i]) - int(min_number[len(min_number) - 1 - i])
                difference.append(number)
                xchange = True
            else:
                number = (10 + int(max_number[len(max_number) - 1 - i])) - int(min_number[len(min_number) - 1 - i]) - 1
                difference.append(number)
    for x in range(0, len(max_number)-len(min_number)):
        if xchange is False:
            difference.append(int(max_number[len(max_number) - len(min_number) - 1 - x]))
        if xchange is True:
            number = int(max_number[len(max_number) - len(min_number) - 1 - x]) - 1
            if number < 0:
                number = (10 + int(max_number[len(max_number) - len(min_number) - 1 - x])) - 1
                difference.append(number)
            else:
                difference.append(number)
                xchange = False
    work_difference = []
    for j in range(len(difference) - 1, -1, -1):
        work_difference.append(str(difference[j]))
    while work_difference[0] == '0' and len(work_difference) > 1:
        work_difference.pop(0)
    work_difference = ''.join(work_difference)
    return work_difference


# print(BigMinus("50", "50"))
