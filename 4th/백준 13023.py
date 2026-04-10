import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N: 사람 수, M: 친구 관계 수
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

# 무방향 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
found = False

def dfs(node, depth):
    global found

    # 길이 4의 경로를 찾으면 종료
    if depth == 5:
        found = True
        return

    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, depth + 1)
            if found:
                return

    # 백트래킹
    visited[node] = False

for i in range(N):
    dfs(i, 1)
    if found:
        print(1)
        break
else:
    print(0)