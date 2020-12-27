def MatrixTurn(Matrix, M, N, T):
    for a in range(M):
        Matrix[a] = list(Matrix[a])
    print(Matrix)
    if M <= N:
        circles = M // 2
    else:
        circles = N // 2
    for k in range(T):  # количество поворотов
        for m in range(circles):  # количество кругов
            for i in range(m + 1, N - m):
                if i == 1 + m:
                    a = Matrix[m][i - 1]
                else:
                    a = b
                b = Matrix[m][i]
                Matrix[m][i] = a
            for j in range(m + 1, M - m):
                a = b
                b = Matrix[j][N - m - 1]
                Matrix[j][N - m - 1] = a
            for q in range(N - m - 2, m - 1, -1):
                a = b
                b = Matrix[M - m - 1][q]
                Matrix[M - m - 1][q] = a
            for w in range(M - m - 2, m - 1, -1):
                a = b
                b = Matrix[w][m]
                Matrix[w][m] = a
    for i in range(M):
        Matrix[i] = ''.join(Matrix[i])
    return Matrix


# print(MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 4))
# print(MatrixTurn(["1234", "2345", "3456", "4567", "5678", "6789"], 6, 4, 1))
# print(MatrixTurn(["1234567", "2345678", "3456789", "4567891"], 4, 7, 1))
# print(MatrixTurn(["111", "222"], 2, 3, 1))
# print(MatrixTurn(["12", "23"], 2, 2, 1))
# print(MatrixTurn(["12326", "12325", "54316", "64315"], 4, 5, 1))
