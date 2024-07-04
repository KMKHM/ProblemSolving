"""
클레어와 물약
문제: https://www.acmicpc.net/problem/20119
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    ls = list(map(int, input().split()))
    for i in range(ls[0]):
        graph[ls[i+1]].append(ls[-1])
        indegree[ls[-1]] += 1

l = int(input())

y = list(map(int, input().split()))

check = [0] * (n+1)

q = deque(y)

tmp = set()
while q:
    cur = q.popleft()
    tmp.add(cur)
    for v in graph[cur]:
        indegree[v] -= 1
        if not indegree[v]:
            q.append(v)

for i in tmp:
    check[i] = 1
print(sum(check))
for i in range(1, n+1):
    if check[i]:
        print(i, end=" ")