"""
너구리 구구
문제: https://www.acmicpc.net/problem/18126
"""
import sys
sys.setrecursionlimit(10 ** 6)

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


res = 0
visited = [0] * (n+1)
visited[1] = 1

def dfs(start, distance):

    global res

    res = max(distance, res)

    for k, v in graph[start]:
        if not visited[k]:
            visited[k] = 1
            dfs(k, distance + v)
            visited[k] = 0

dfs(1, 0)

print(res)