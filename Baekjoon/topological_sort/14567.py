"""
선수과목 (Prerequisite)
문제: https://www.acmicpc.net/problem/14567
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
check = [0] * (n+1)

for i in range(1, n+1):
    if not indegree[i]:
        q.append([i, 1])
        check[i] = 1

ans = [0] * (n+1)

while q:
    cur, cnt = q.popleft()
    ans[cur] = cnt
    for v in graph[cur]:
        if not check[v]:
            indegree[v] -= 1
            if indegree[v] == 0:
                check[v] = 1
                q.append([v, cnt+1])

print(*ans[1:])