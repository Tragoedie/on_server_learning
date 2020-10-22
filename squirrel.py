def squirrel(N):
    if N <= 0:
        return -1
    else:
        factorial = 1
        for i in range(1, N+1):
            factorial *= i
        while factorial > 9:
            factorial = factorial // 10
        return factorial
