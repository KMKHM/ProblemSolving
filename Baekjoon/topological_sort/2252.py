"""
줄 세우기
문제: https://www.acmicpc.net/problem/2252
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree, check = [0] * (n+1), [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)
        check[i] = 1

while q:
    cur = q.popleft()
    print(cur, end=" ")

    for v in graph[cur]:
        if not check[v]:
            indegree[v] -= 1
            if not indegree[v]:
                check[v] = 1
                q.append(v)