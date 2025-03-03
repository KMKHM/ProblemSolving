"""
케빈 베이컨의 6단계 법칙
문제: https://www.acmicpc.net/problem/1389
"""
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [set() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(start, end):
    q = deque()
    q.append([start, 0])
    check = [0] * (n+1)
    check[start] = 1
    while q:
        cur, cnt = q.popleft()
        if cur == end:
            return cnt
        for v in graph[cur]:
            if not check[v]:
                check[v] = 1
                q.append([v, cnt + 1])
    return -1


val = sys.maxsize

visited = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if not visited[i][j]:
            visited[i][j] = bfs(i, j)
            visited[j][i] = visited[i][j]

ans = 0

for i in range(1, n+1):
    tmp = sum(visited[i])
    if val > tmp:
        val = tmp
        ans = i

print(ans)
