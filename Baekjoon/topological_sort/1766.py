"""
문제집
문제: https://www.acmicpc.net/problem/1766
"""
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    cur = heapq.heappop(q)
    print(cur, end=" ")
    for v in graph[cur]:
        indegree[v] -= 1
        if not indegree[v]:
            heapq.heappush(q, v)