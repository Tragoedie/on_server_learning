def BalancedParentheses(N):
    work_massive = []
    massive = []
    for j in range(2 * N):
        work_massive.append('')
    if N > 0:
        BalancedParentheses_2(work_massive, 0, N, 0, 0, massive)
    massive.pop(len(massive) - 1)
    massive = ''.join(massive)
    return massive
    # print(massive)


def BalancedParentheses_2(work_massive, index, N, open_parenthesis, close_parenthesis, massive):
    if close_parenthesis == N:
        for i in range(len(work_massive)):
            massive.append(work_massive[i])
        massive.append(' ')
    else:
        if open_parenthesis > close_parenthesis:
            work_massive[index] = ')'
            BalancedParentheses_2(work_massive, index + 1, N, open_parenthesis, close_parenthesis + 1, massive)
        if open_parenthesis < N:
            work_massive[index] = '('
            BalancedParentheses_2(work_massive, index + 1, N, open_parenthesis + 1, close_parenthesis, massive)


# N = 5
# print(BalancedParentheses(N))
