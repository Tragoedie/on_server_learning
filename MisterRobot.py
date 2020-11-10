def MisterRobot(N, data):
    x_change = False
    y_change = False
    while x_change is False and y_change is False:
        x_change = True
        y_change = True
        for i in range(N - 2):
            counter = 0
            while data[i] > data[i+1] or data[i+1] > data[i+2]:
                number = data[i]
                data[i] = data[i + 1]
                data[i + 1] = data[i + 2]
                data[i + 2] = number
                counter += 1
                x_change = False
                if counter == 3:
                    break
            if counter == 3:
                while data[i] > data[i+1]:
                    number = data[i]
                    data[i] = data[i+1]
                    data[i+1] = data[i+2]
                    data[i+2] = number
        for j in range(len(data)-2):
            if data[j] > data[j+1]:
                y_change = False
    for x in range(len(data)):
        if data[len(data)-2] > data[len(data)-1]:
            return False
    return True


# N = 10
# data = [1, 2, 3, 4, 5, 7, 6]
# data = [2, 3, 1, 7, 4, 6, 5]
# data = [1, 3, 4, 5, 6, 2, 7]
# print(MisterRobot(N, data))
