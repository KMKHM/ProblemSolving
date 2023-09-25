"""
무기 공학
문제: https://www.acmicpc.net/problem/18430
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

if n*m < 3:
    print(0)
    sys.exit(0)

# ㄱ자 방향
dir = {1: [(0, -1), (1, 0)],
       2: [(0, -1), (-1, 0)],
       3: [(0, 1), (1, 0)],
       4: [(0, 1), (-1, 0)]}


# 방문여부
visited = [[0]*m for _ in range(n)]

ans = 0

res = []

def bt(x, y, val):
    global ans

    if y == m:
        x, y = x+1, 0
    if x == n:
        ans = max(ans, val)
        return

    if not visited[x][y]:
        for i in range(1, 5):
            udx, udy, rlx, rly = x + dir[i][0][0], y + dir[i][0][1], x + dir[i][1][0], y + dir[i][1][1]
            if 0<=udx<n and 0<=udy<m and 0<=rlx<n and 0<=rly<m and not visited[udx][udy] and not visited[rlx][rly]:
                visited[x][y], visited[udx][udy], visited[rlx][rly] = 1, 1, 1
                bt(x, y + 1, val + board[x][y] * 2 + board[udx][udy] + board[rlx][rly])
                visited[x][y], visited[udx][udy], visited[rlx][rly] = 0, 0, 0
    bt(x, y + 1, val)


bt(0, 0, 0)
print(ans)




