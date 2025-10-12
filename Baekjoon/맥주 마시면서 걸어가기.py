"""
https://www.acmicpc.net/problem/9205
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(sx, sy, ex, ey, store):
    q = deque()
    q.append((sx, sy))
    visited = [0] * len(store)
    while q:
        cx, cy = q.popleft()
        if abs(cx-ex) + abs(cy-ey) <= 1000:
            return "happy"
        for i in range(len(store)):
            hx, hy = store[i][0], store[i][1]
            if abs(cx-hx) + abs(cy-hy) <= 1000 and not visited[i]:
                visited[i] = 1
                q.append((hx, hy))
    return "sad"


for _ in range(int(input())):
    # 편의점 수
    n = int(input())
    # 상근이네집
    sx, sy = map(int, input().split())
    # 편의점
    availabe = []

    for _ in range(n):
        availabe.append(list(map(int, input().split())))
    availabe.sort(key=lambda x: (x[0], x[1]))

    # 목표 지점
    ex, ey = map(int, input().split())

    print(bfs(sx, sy, ex, ey, availabe))