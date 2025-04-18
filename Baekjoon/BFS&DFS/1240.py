"""
노드사이의 거리
문제: https://www.acmicpc.net/problem/1240
"""
import sys
from collections import deque

input = sys.stdin.readline

# 노드의 개수와 노드쌍의 개수 입력
n, m = map(int, input().split())

# 그래프
graph = [[] for _ in range(n+1)]

# 거리 입력
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])

# BFS&DFS 함수
def bfs(start, end, visited):
    q = deque()
    # 초기 거리는 0이다.
    q.append([start, 0])
    visited[start] = 1

    while q:
        now, d = q.popleft()
        # 만약 end가 pop되면 거리 리턴
        if now == end:
            return d

        # 연결된 노드중에
        for next, cost in graph[now]:
            if visited[next] == 0:
                # 방문 처리 후, start에서 next까지 거리를 큐에 넣는다.
                visited[next] = 1
                q.append([next, d + cost])


for _ in range(m):
    x, y = map(int, input().split())
    visited = [0] * (n+1)
    print(bfs(x, y, visited))