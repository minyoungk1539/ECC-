import sys
input = sys.stdin.readline #속도 증가

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def dfs(idx, total):
    global count

    # 끝까지 확인했으면 합이 S인지 검사
    if idx == N:
        if total == S:
            count += 1
        return

    # 현재 원소를 선택하는 경우
    dfs(idx + 1, total + arr[idx])

    # 현재 원소를 선택하지 않는 경우
    dfs(idx + 1, total)

dfs(0, 0)

# 공집합이 포함된 경우 제외
if S == 0:
    count -= 1

print(count)