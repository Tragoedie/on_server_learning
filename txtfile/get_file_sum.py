def get_file_sum(file_name):

    try:
        with open((str(file_name)+'.txt')) as list_1:
            sum = 0
            for line_1 in list_1:
                try:
                    sum += int(line_1.rstrip())
                except ValueError:
                    print("Ошибка типа")
                    continue
        print("Step 3 - сумма чисел первого файла:", sum)
    except FileNotFoundError:
        print("Invilid file")
        sum = 0

    return sum
