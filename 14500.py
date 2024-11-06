"""
테트로미노
문제: https://www.acmicpc.net/problem/14500
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

check = [[0] * m for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

res = 0

def bt(x, y, value, level):
    global res

    if level == 4:
        res = max(res, value)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
            check[nx][ny] = 1
            bt(nx, ny, value + board[nx][ny], level + 1)
            check[nx][ny] = 0

def cross(x, y):
    global res

    tmp=board[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m):
            return
        tmp += board[nx][ny]

    arr=[tmp]*4
    # arr = [10, 10, 10, 10]
    # arr = [9, 8, 8, 7]

    for k in range(4):
        na, nb = x + dx[k], y + dy[k]
        arr[k] -= board[na][nb]

    res = max(res, max(arr))


for i in range(n):
    for j in range(m):
        check[i][j] = 1
        bt(i, j, 0, 0)
        cross(i, j)
        check[i][j] = 0

print(res)