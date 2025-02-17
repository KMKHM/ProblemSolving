"""
텔레포트 3
문제: https://www.acmicpc.net/problem/12908
"""
import sys
from collections import Counter, deque

input = sys.stdin.readline

xs, ys = map(int, input().split())

xe, ye = map(int, input().split())

# 1 sec
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

# 10 sec
teleport = Counter()

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    teleport[(x1, y1)] = (x2, y2)
    teleport[(x2, y2)] = (x1, y1)

visit = set()

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visit.add((x, y))

    while q:
        cx, cy, cur = q.popleft()
        if cx == xe and cy == ye:
            return cur

        if (cx, cy) in teleport:
            tx, ty = teleport[(cx, cy)]
            if (tx, ty) not in visit:
                visit.add((tx, ty))
                q.append([tx, ty, cur + 10])

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (nx, ny) not in visit:
                visit.add((nx, ny))
                q.append([nx, ny, cur + 1])
    return -1

print(bfs(xs, ys))
