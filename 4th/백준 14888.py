N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -10**9
min_value = 10**9

def dfs(idx, current, p, m, mu, d):
    global max_value, min_value

    # 숫자를 끝까지 다 사용한 경우
    if idx == N:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return

    # 덧셈
    if p > 0:
        dfs(idx + 1, current + nums[idx], p - 1, m, mu, d)

    # 뺄셈
    if m > 0:
        dfs(idx + 1, current - nums[idx], p, m - 1, mu, d)

    # 곱셈
    if mu > 0:
        dfs(idx + 1, current * nums[idx], p, m, mu - 1, d)

    # 나눗셈: C++14 방식처럼 0을 향해 버림
    if d > 0:
        if current < 0:
            dfs(idx + 1, -(-current // nums[idx]), p, m, mu, d - 1)
        else:
            dfs(idx + 1, current // nums[idx], p, m, mu, d - 1)

dfs(1, nums[0], plus, minus, mul, div)

print(max_value)
print(min_value)