"""
트리의 지름
문제: https://www.acmicpc.net/problem/1167
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

v = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(v):
    ls = list(map(int, input().split()))
    u = ls[0]
    ls = ls[1:len(ls)-1]
    for i in range(0, len(ls), 2):
        a, c = ls[i], ls[i+1]
        graph[u].append([a, c])

visited = [0] * (v+1)
dist = [0] * (v+1)
def dfs(start, cur):
    visited[start] = 1
    dist[start] = cur
    for vertex, cost in graph[start]:
        if not visited[vertex]:
            dfs(vertex, cur + cost)

dfs(1, 0)

val = 0
node = 0
for i in range(1, v+1):
    if dist[i] > val:
        node = i
        val = dist[i]

dist = [0] * (v+1)
visited = [0] * (v+1)
dfs(node, 0)

print(max(dist))