def solution(money):
    def rob_linear(houses):
        dp = [0] * len(houses)

        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, len(houses)):
            dp[i] = max(
                dp[i - 1],              # 현재 집을 털지 않음
                dp[i - 2] + houses[i]   # 현재 집을 털음
            )

        return dp[-1]

    # 첫 번째 집 포함 가능, 마지막 집 제외
    case1 = rob_linear(money[:-1])

    # 첫 번째 집 제외, 마지막 집 포함 가능
    case2 = rob_linear(money[1:])

    return max(case1, case2)