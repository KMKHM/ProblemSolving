"""
https://www.acmicpc.net/problem/15732
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k, d = map(int, input().split())

arr = [0] * (n+1)

acorn = []

for _ in range(k):
    acorn.append(list(map(int, input().split())))

acorn.sort()
visited = [0] * k

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if arr[x] >= k:
            return x

        for i in range(k):
            if not visited[i]:
                visited[i] = 1
                a, b, c = acorn[i]
                for j in range(a, b+1, c):
                    arr[j]+=1
                q.append(a)
print(bfs(0))





