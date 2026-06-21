def solution(N, number):
    # N 하나만 사용해서 number를 만들 수 있는 경우
    if N == number:
        return 1

    # dp[i] = N을 i번 사용해서 만들 수 있는 모든 수
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # N, NN, NNN처럼 이어 붙인 수
        dp[i].add(int(str(N) * i))

        # N 사용 횟수를 j개와 i-j개로 나누어 계산
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)

                    # 0으로 나누는 경우 제외
                    if b != 0:
                        # 프로그래머스 문제에서는 정수 나눗셈 사용
                        dp[i].add(int(a / b))

        if number in dp[i]:
            return i

    return -1