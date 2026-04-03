#노드 다른노드 거리 -1 -> weight 계산
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    node = arr[0]

    for k in range(1, len(arr), 2):
        if arr[k] == -1:
            break
        node2 = arr[k]
        w = arr[k + 1]
        graph[node].append((node2, w))

def dfs(start):
    stack = [(start, 0)]
    visited = [False] * (V + 1)
    visited[start] = True

    far_node = start
    max_dist = 0

    while stack:
        now, dist = stack.pop()

        if dist > max_dist:
            max_dist = dist
            far_node = now

        for nxt, w in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, dist + w))

    return far_node, max_dist

# 1번 노드에서 가장 먼 노드 찾기
far_node, _ = dfs(1)

# 그 노드에서 다시 가장 먼 거리 찾기
_, answer = dfs(far_node)

print(answer)