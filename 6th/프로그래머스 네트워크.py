from collections import deque

def bfs(start, visited, computers, n):  #bfs 정의
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for next in range(n):
            if computers[v][next] == 1 and not visited[next]:
                visited[next] = True
                queue.append(next)

def solution(n, computers):

    visited = [False] * n

    count = 0

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            count += 1  #bfs를 불러올 때마다 추가

    answer = count
    return answer