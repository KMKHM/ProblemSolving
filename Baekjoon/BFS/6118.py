"""
숨바꼭질
https://www.acmicpc.net/problem/6118
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

nums = [0] * (n+1)
check = [0] * (n+1)
def bfs(start):
    q = deque()
    q.append([start, 0])
    check[start] = 1
    while q:
        cur, cnt = q.popleft()
        nums[cur] = cnt

        for v in graph[cur]:
            if not check[v]:
                check[v] = 1
                q.append([v, cnt + 1])

bfs(1)
val = max(nums)

a = 0
b = val
c = sum(1 for i in range(2, n+1) if nums[i] == val)

for i in range(2, n+1):
    if nums[i] == val:
        a = i
        break
print(a, b, c)