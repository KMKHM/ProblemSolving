"""
트리와 쿼리
문제: https://www.acmicpc.net/problem/15681
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]



for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

query = []
for _ in range(q):
    u = int(input())
    query.append(u)

dp = [0] * (n+1)

visited = [0] * (n + 1)

def dfs(x):
    visited[x] = 1
    dp[x] = 1
    for vertex in graph[x]:
        if visited[vertex] == 0:
            dfs(vertex)
            dp[x] += dp[vertex]

dfs(r)

for sol in query:
    print(dp[sol])

