def TankRush(H1, W1, S1, H2, W2, S2):
    massive = []
    map = []
    tank = []
    for a in range(len(S1)):
        if S1[a] != ' ':
            massive.append(S1[a])
        else:
            map.append(massive)
            massive = []
    map.append(massive)
    massive = []
    for b in range(len(S2)):
        if S2[b] != ' ':
            massive.append(S2[b])
        else:
            tank.append(massive)
            massive = []
    tank.append(massive)
    print(map)
    print(tank)
    xchange = False
    for i in range(0, H1-H2+1):
        for j in range(0, W1-W2+1):
            if map[i][j] == tank[0][0]:
                coordinate_x = i
                coordinate_y = j
                xchange = True
                for x in range(coordinate_x, coordinate_x+H2):
                    for y in range(coordinate_y, coordinate_y+W2):
                        if map[x][y] != tank[x-coordinate_x][y-coordinate_y]:
                            xchange = False
                            break
                    if xchange is False:
                        break
                if xchange is True:
                    return True
    return False


# print(TankRush(4, 6, '029402 560202 029694 780288',2,2,'02 94'))