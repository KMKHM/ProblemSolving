"""
작업
문제: https://www.acmicpc.net/problem/21937
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

v = int(input())

stack = [v]

visited = [0] * (n+1)
visited[v] = 1

res = 0

while stack:
    cur = stack.pop()

    for i in graph[cur]:
        if not visited[i]:
            visited[i] = 1
            res += 1
            stack.append(i)

print(res)