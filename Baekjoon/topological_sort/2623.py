"""
음악프로그램
문제: https://www.acmicpc.net/problem/2623
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

indegree = [0 for _ in range(n + 1)]

q = deque()

for _ in range(m):
    c, *ls = map(int, input().split())

    for i in range(c-1):
        graph[ls[i]].append(ls[i + 1])
        indegree[ls[i+1]] += 1

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

res=[]

while q:
    cur = q.popleft()
    res.append(cur)
    for v in graph[cur]:
        indegree[v] -= 1
        if not indegree[v]:
            q.append(v)

if len(res) != n:
    print(0)
else:
    for num in res:
        print(num)