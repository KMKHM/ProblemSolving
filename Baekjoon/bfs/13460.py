"""
구슬탈출 2
문제: https://www.acmicpc.net/problem/13460
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

visited1 = [[0] * m for _ in range(n)]
visited2 = [[0] * m for _ in range(n)]

red = [(x, y) for x in range(n) for y in range(m) if board[x][y] == "R"][0]
blue = [(x, y) for x in range(n) for y in range(m) if board[x][y] == "B"][0]
end = [(x, y) for x in range(n) for y in range(m) if board[x][y] == "O"][0]

def check(a, b):
    if a >= n or a < 0 or b >=m or b < 0:
        return False
    return True
ans = 0

def bfs(x1, y1, x2, y2):
    global ans
    q1 = deque()
    q2 = deque()
    q1.append((x1, y1))
    q2.append((x2, y2))
    visited1[x1][y1] = 1
    visited2[x2][y2] = 1
    while q1 and q2:
        if q1:
            now_x1, now_y1 = q1.popleft()
        if q2:
            now_x2, now_y2 = q2.popleft()
        for i in range(4):
            nx, ny = now_x1, now_y1
            nx2, ny2 = now_x2, now_y2
            while True:
                nx += dx[i]
                ny += dy[i]
                if check(nx, ny):
                    if board[nx][ny] == "#" or board[nx][ny] == "B":
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if board[nx][ny] == "O":
                        ans = visited1[now_x1][now_y1]
                        return visited1[now_x1][now_y1]
                if not check(nx, ny):
                    nx -= dx[i]
                    ny -= dy[i]
                    break

            if not visited1[nx][ny]:
                visited2[nx][ny] = visited2[now_x1][now_y1] + 1
                q1.append((nx, ny))
            if ans == 1:
                q1.clear()

            while True:
                nx2 += dx[i]
                ny2 += dy[i]
                if check(nx2, ny2):
                    if board[nx2][ny2] == "#":
                        nx2 -= dx[i]
                        ny2 -= dy[i]
                        break
                    if board[nx2][ny2] == "O":
                        ans = -1
                if not check(nx2, ny2):
                    nx2 -= dx[i]
                    ny2 -= dy[i]
                    break
            if not visited2[nx2][ny2]:
                visited2[nx2][ny2] = visited2[now_x1][now_y1] + 1
                q1.append((nx2, ny2))
    return -1

print(bfs(red[0], red[1], blue[0], blue[1]))
print(ans)






