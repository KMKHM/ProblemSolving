"""
거울 설치
문제: https://www.acmicpc.net/problem/2151
"""
import sys

input = sys.stdin.readline

n = int(input())


arr = []
possible = []
door = []

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

for i in range(n):
    ls = list(input().rstrip())
    arr.append(ls)
    for j in range(n):
        if arr[i][j] == "!":
            possible.append([i, j])
        if arr[i][j] == "#":
            door.append([i, j])

res = 1e9

sx, sy = door[0]
ex, ey = door[1]

def turn(x, y, dir):
    if dir == 1:
        if x == 1:
            x = 0
            y = -1
        elif x == -1:
            x = 0
            y = 1
        elif y == 1:
            x = -1
            y = 0
        elif y == -1:
            x = 1
            y = 0
    else:
        x, y = y, x
    return x, y

dir = []

for i in range(4):
    nx, ny = sx + dx[i], sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] != "*":
            dir.append([dx[i], dy[i]])

visited = [[0] * n for _ in range(n)]
visited[sx][sy] = 1

def backtracking(x, y, cnt, dirx, diry):
    global res

    if arr[x][y] == "*":
        return

    if x == ex and y == ey:
        res = min(res, cnt)
        return

    if arr[x][y] == "!":

        dirx, diry = turn(dirx, diry, 1)
        if not visited[x+dirx][y+diry]:
            visited[x+dirx][y+diry] = 1
            backtracking(x+dirx, y+diry, cnt + 1, dirx, diry)
            visited[x+dirx][y+diry] = 0

        dirx, diry = turn(dirx, diry, 0)
        if not visited[x+dirx][y+diry]:
            visited[x+dirx][y+diry] = 1
            backtracking(x+dirx, y+diry, cnt + 1, dirx, diry)
            visited[x+dirx][y+diry] = 0

    elif arr[x][y] == ".":
        if not visited[x+dirx][y+diry]:
            visited[x+dirx][y+diry] = 1
            backtracking(x + dirx, y + diry, cnt, dirx, diry)
            visited[x+dirx][y+diry] = 0

for ix, iy in dir:
    visited[sx+ix][sy+iy] = 1
    backtracking(sx+ix, sy+iy, 0, ix, iy)
    visited[sx+ix][sy+iy] = 0

print(res)





