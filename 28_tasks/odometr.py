def odometer(oksana):
    IsArrayValid = len(oksana) % 2 != 0 or len(oksana) < 2 or oksana[0] < 0 or oksana[1] <= 0
    if IsArrayValid:
        return -1
    S = oksana[0] * oksana[1]
    for i in range(2, len(oksana), 2):
        if oksana[i] < 0 or oksana[i+1] <= oksana[i-1]:
            return -1
        S += oksana[i]*(oksana[i+1]-oksana[i-1])
    return S
