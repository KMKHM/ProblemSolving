"""
직사각형 탈출
문제: https://www.acmicpc.net/problem/16973
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
wall = [(x, y) for x in range(n) for y in range(m) if board[x][y] == 1]


# 직사각형 = h X w / 시작 = (s1, s2) => 직사각형의 가장 왼쪽 위칸임 / 목표 = (f1, f2)
h, w, s1, s2, f1, f2 = map(int, input().split())

# 이동방향
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

# 방문
visited = [[0] * m for _ in range(n)]

# 직사각형이 격자판 내부에 있는지 확인하는 함수
def check(a, b):
    for x, y in wall:
        if a <= x < a + h and b <= y < b + w:
            return False
    return True

# 너비우선탐색
def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 1
    while q:
        now_x, now_y, now_cnt = q.popleft()
        if (now_x, now_y) == (f1 - 1, f2 - 1):
            return now_cnt
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (0 <= nx + h -1 < n) and (0 <= ny + w -1 < m) and not visited[nx][ny]:
                if check(nx, ny):
                    visited[nx][ny] = 1
                    q.append((nx, ny, now_cnt + 1))
    return -1

print(bfs(s1 - 1, s2 - 1))