def addition(number_1, number_2):
    try:
        with open((str(number_1)+'.txt')) as list_1:
            sum_1 = 0
            for line_1 in list_1:
                try:
                    sum_1 += int(line_1.rstrip())
                except ValueError:
                    print("Ошибка типа")
                    continue
        print("Step 3 - сумма чисел первого файла:", sum_1)
    except FileNotFoundError:
        print("Invilid file")
        sum_1 = 0
    try:
        with open((str(number_2)+'.txt')) as list_2:
            sum_2 = 0
            for line_2 in list_2:
                try:
                    sum_2 += int(line_2.rstrip())
                except ValueError:
                    print("Ошибка типа")
                    continue
        print("Step 4 - сумма чисел второго файла:", sum_2)
    except FileNotFoundError:
        print("invilid file")
        sum_2 = 0

    sum_common = sum_1 + sum_2
    return sum_common






