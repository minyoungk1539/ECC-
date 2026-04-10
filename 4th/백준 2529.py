import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

visited = [False] * 10  # 숫자 중복 사용 방지
min_num = ""
max_num = ""

# 부등호 조건 확인 함수
def check(a, b, op):
    if op == '<':
        return a < b
    return a > b

def dfs(depth, path):
    global min_num, max_num

    # k+1개의 숫자를 모두 채운 경우
    if depth == k + 1:
        num = ''.join(map(str, path))
        if not min_num:  # 처음 나온 값이 최소값
            min_num = num
        max_num = num     # 계속 갱신되므로 마지막이 최대값
        return

    # 0~9 숫자를 하나씩 선택
    for num in range(10):
        if not visited[num]:
            # 첫 숫자이거나 부등호 조건 만족 시
            if depth == 0 or check(path[-1], num, signs[depth - 1]):
                visited[num] = True
                path.append(num)

                dfs(depth + 1, path)

                # 백트래킹
                path.pop()
                visited[num] = False

dfs(0, [])

print(max_num)
print(min_num)