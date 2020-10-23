def ConquestCampaign (N, M, L, battalion):
    kingdom_s = []
    for i in range(N):
        kingdom = []
        for j in range(M):
            kingdom.append(0)
        kingdom_s.append(kingdom)
    for a in range(L):
        coordinate_x = battalion[a * 2]
        coordinate_y = battalion[a * 2 + 1]
        kingdom_s[coordinate_x - 1][coordinate_y - 1] = 1
    # print(kingdom_s)
    day = 1
    for a in range(N):
        for b in range(M):
            while kingdom_s[a][b] == 0:
                day += 1
                for i in range(N):
                    for j in range(M):
                        if kingdom_s[i][j] == 1:
                            kingdom_s[i][j] = 2
                for x in range(N):
                    for y in range(M):
                        if kingdom_s[x][y] == 2:
                            if y > 0 and kingdom_s[x][y-1] == 0:
                                kingdom_s[x][y-1] = 1
                            if y + 1 < M and kingdom_s[x][y+1] == 0:
                                kingdom_s[x][y+1] = 1
                            if x > 0 and kingdom_s[x - 1][y] == 0:
                                kingdom_s[x - 1][y] = 1
                            if x + 1 < N and kingdom_s[x+1][y] == 0:
                                kingdom_s[x+1][y] = 1
    return day


                # print(day)
                # print(kingdom_s)
# N = 3
# M = 4
# L = 3
# battalion = [2, 2, 2, 2, 3, 4]
# print(ConquestCampaign(N, M, L, battalion))
