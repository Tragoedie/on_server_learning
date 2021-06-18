def MixTele(N, Tele):
    x_change = True
    while x_change:
        x_change = False
        for i in range(N - 1):
            if Tele[i] > Tele[i + 1]:
                Tele[i], Tele[i + 1] = Tele[i + 1], Tele[i]
                x_change = True

def MadMax(N, Tele):
    MixTele(N, Tele)
    #print(Tele)
    Tele[N//2], Tele[N-1] = Tele[N-1], Tele[N//2]
    #print(Tele)
    y_change = True
    while y_change:
        y_change = False
        for j in range(N//2+1, N-2):
            if Tele[j] < Tele[j+1]:
                Tele[j], Tele[j+1] = Tele[j+1], Tele[j]
                y_change = True
    #print(Tele)
    return Tele

# import random
# N = 11
# Tele = []
# for i in range (N):
    # Tele.append(random.randint(0, 255))
# print(Tele)
# MadMax(N, Tele)
