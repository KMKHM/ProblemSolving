"""
암벽 등반
문제: https://www.acmicpc.net/problem/2412
"""
import sys
from collections import deque

input = sys.stdin.readline

n, t = map(int, input().split())

point = set()

for _ in range(n):
    x, y = map(int, input().split())
    point.add((x, y))


q = deque()
q.append([0, 0, 0])

while q:
    curX, curY, cnt = q.popleft()

    if curY == t:
        print(cnt)
        sys.exit(0)

    for i in range(-2, 3):
        for j in range(-2, 3):
            nextX, nextY = curX + i, curY + j
            if (nextX, nextY) in point:
                q.append([nextX, nextY, cnt + 1])
                point.remove((nextX, nextY))



