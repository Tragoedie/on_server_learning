def exponentional(N, M):
    if M == 0:
        return 1
    return N * exponentional(N, M - 1)


print(exponentional(2, 3))
