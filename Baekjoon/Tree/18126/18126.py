"""
너구리 구구
문제: https://www.acmicpc.net/problem/18126
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    sys.exit(0)

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def bfs(start, end, visited):
    visited[start] = 1
    q = deque()
    q.append([start, 0])

    while q:
        cur, dis = q.pop()
        if cur == end:
            return dis
        for nex, next_dis in graph[cur]:
            if not visited[nex]:
                visited[nex] = 1
                q.append([nex, dis + next_dis])
    return -1

res = 0
for i in range(2, n+1):
    res = max(bfs(1, i, [0]*(n+1)), res)

print(res)