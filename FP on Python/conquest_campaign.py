from pymonad import List
from itertools import groupby


day_pass = lambda pos: List(
    (pos[0], pos[1]),
    (pos[0] - 1, pos[1]),
    (pos[0] + 1, pos[1]),
    (pos[0], pos[1] - 1),
    (pos[0], pos[1] + 1),
)


def ConquestCampaign(N, M, battalion, counter=1):
    if counter == 1:
        battalion = List(*zip(*[iter(battalion)] * 2))

    if_valid = lambda pos: List(pos) if 1 <= pos[0] <= N and 1 <= pos[1] <= M else List()

    if battalion.__len__() == N * M:
        print(counter)
    else:
        battalion = battalion >> day_pass >> if_valid
        battalion = List(*(item for item, _ in groupby(sorted(battalion))))
        counter = counter + 1
        ConquestCampaign(N, M, battalion, counter)

ConquestCampaign(3, 4, [2, 2, 3, 4])