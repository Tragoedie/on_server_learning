def CalcPercentage(N, Votes, percent_votes):
    summ_votes = 0
    for i in range(N):
        summ_votes += Votes[i]
    for j in range(N):
        percent = Votes[j] / summ_votes * 100
        percent_votes.append(percent)

def MassVote(N, Votes):
    percent_votes = []
    CalcPercentage(N, Votes, percent_votes)
    max_votes = percent_votes[0]
    for x in range(1, N):
        if percent_votes[x] > max_votes:
            max_votes = percent_votes[x]
    count = 0
    winner = 0
    result = ''
    for y in range(N):
        if max_votes == percent_votes[y]:
            count += 1
            winner = y + 1
    if count > 1:
        result = "no winner"
    else:
        if max_votes > 50:
            result = "majority winner " + str(winner)
        else:
            result = "minority winner " + str(winner)
    return result

# N = 4
# Votes = [111, 111, 110, 110]
# print(MassVote(N, Votes))
