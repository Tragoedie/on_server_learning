def addition(number_1, number_2):
    list_1 = open(str(number_1)+'.txt')
    sum_1 = 0
    for line_1 in list_1:
        s = list_1.readline()
        if s == "":
            continue
        sum_1 += int(line_1.rstrip())
    list_1.close()
    print("Step 3 - сумма чисел первого файла:", sum_1)
    list_2 = open(str(number_2)+'.txt')
    sum_2 = 0
    for line_2 in list_2:
        s_2 = list_2.readline()
        if s_2 == "":
            continue
        sum_2 += int(line_2.rstrip())
    print("Step 4 - сумма чисел второго файла:", sum_2)
    list_2.close()
    sum_common = sum_1 + sum_2
    return sum_common
