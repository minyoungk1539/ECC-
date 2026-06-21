def solution(m, n, puddles):
    can = [[0] * (m + 1) for _ in range(n + 1)]
    can[1][1] = 1

    for l in range(1, n + 1):
        for i in range(1, m + 1):

            if [i, l] in puddles:
                can[l][i] = 0
                continue

            if (i, l) == (1, 1):
                continue

            if i > 1:
                can[l][i] += can[l][i - 1]

            if l > 1:
                can[l][i] += can[l - 1][i]

            can[l][i] %= 1000000007

    return can[n][m]