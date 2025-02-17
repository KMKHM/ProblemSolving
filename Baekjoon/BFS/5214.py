"""
환승
문제: https://www.acmicpc.net/problem/5214
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())

graph = [set() for _ in range(n+1)]

for _ in range(m):
    nums = list(map(int, input().split()))
    for a in nums:
        for b in nums:
            if a == b:
                continue
            graph[a].add(b)
            graph[b].add(a)

visited = [0] * (n+1)

def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        if now == end:
            return visited[end]
        for v in graph[now]:
            if not visited[v]:
                visited[v] = visited[now] + 1
                q.append(v)
    return -1

print(bfs(1, n))
