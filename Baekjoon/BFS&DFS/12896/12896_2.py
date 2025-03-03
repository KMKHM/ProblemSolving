"""
스크루지 민호
https://www.acmicpc.net/problem/12896
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
from collections import Counter

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append([b, 1])
    graph[b].append([a, 1])

visited = [0] * (n+1)

distance = Counter()

def dfs(start, cnt):

    distance[start] = cnt
    visited[start] = 1

    for vertex, cost in graph[start]:
        if not visited[vertex]:
            dfs(vertex, cnt + cost)

dfs(1, 0)

max_distance = max(distance.values())

node = 0

for key, value in distance.items():
    if value == max_distance:
        node = key
        break

distance = Counter()
visited = [0] * (n+1)
dfs(node, 0)

print((max(distance.values()) + 1)//2)
