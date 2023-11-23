"""
관악산 등산
문제: https://www.acmicpc.net/problem/14699
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

height = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    if height[a] > height[b]:
        graph[b].append(a)
    else:
        graph[a].append(b)

course = [0] * (n+1)

visited = [0] * (n+1)


# def dfs(start, cnt):
#
#     visited[start] = 1
#
#
#     if not graph[start]:
#         course[start] = max(course[start], cnt)
#         return
#
#     for v in graph[start]:
#         if not visited[v]:
#             dfs(v, cnt + 1)
def bfs(start, cnt):
    q = deque()
    visited[start] = 1
    q.append([start, cnt])
    while q:
        now, now_c = q.popleft()
        print(now, now_c)
        # course[start] = max(course[start], now_c)
        for v in graph[now]:
            if not visited[v]:
                visited[v] = 1
                q.append([v, now_c + 1])


print(graph)

print(bfs(2, 1))
# dfs(1, 1)
print(course)

