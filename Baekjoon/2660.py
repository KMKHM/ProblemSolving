"""
회장뽑기
문제: https://www.acmicpc.net/problem/2660
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

max_len = 0

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1] * (n+1)
    visited[start] = 0

    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if visited[v] == -1:
                visited[v] = visited[cur] + 1
                q.append(v)
    return max(visited)

min_val = n
arr = []
for i in range(1, n+1):
    arr.append(bfs(i))

min_val = min(arr)
res=[]

for i in range(n):
    if arr[i] == min_val:
        res.append(i+1)

print(min_val, len(res))
print(*res)