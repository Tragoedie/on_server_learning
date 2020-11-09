def Unmanned(L, N, track):
    car_stop = track[0][0]
    if L <= track[0][0]:
        return L
    for i in range(N):
        traffic_light = track[i][1]
        counter = False
        while car_stop >= traffic_light:
            if counter is False:
                traffic_light += track[i][2]
                counter = True
            else:
                traffic_light += track[i][1]
                counter = False
        if counter is False:
            difference = traffic_light - car_stop
            car_stop = car_stop + difference
        if i < (N-1):
            car_stop += track[i+1][0] - track[i][0]
        else:
            difference = L - track[i][0]
            car_stop += difference
    return car_stop


# print(Unmanned(10, 2, [[11,5,5],[15,2,2]]))
