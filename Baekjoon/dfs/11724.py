"""
연결 요소의 개수
문제: https://www.acmicpc.net/problem/11724
"""
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0]*(n + 1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0

def dfs(start):
    visited[start] = 1
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)