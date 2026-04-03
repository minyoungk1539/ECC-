#노드 다른노드 거리 -> weight 계산
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node, node2, w = map(int, input().split())
    graph[node].append((node2, w))
    graph[node2].append((node, w))

def dfs(start):
    stack = [(start, 0)]
    visited = [False] * (n + 1)
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

far_node, _ = dfs(1)
_, answer = dfs(far_node)

print(answer)