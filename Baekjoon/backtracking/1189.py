"""
컴백홈
문제: https://www.acmicpc.net/problem/1189
"""
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

check = [[0] * c for _ in range(r)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

ans = 0

def bt(x, y, cnt):
    global ans

    check[x][y] = 1

    if (x, y) == (0, c-1):
        if cnt == k:
            ans += 1
            return
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not check[nx][ny] and board[nx][ny] != "T":
            check[nx][ny] = 1
            bt(nx, ny, cnt + 1)
            check[nx][ny] = 0


bt(r-1, 0, 1)

print(ans)