"""
NM과 K (1)
문제: https://www.acmicpc.net/problem/18290
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

check = [[0]*m for _ in range(n)]

ans = -sys.maxsize

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def possible(a, b):
    for d in range(4):
        na, nb = a + dx[d], b + dy[d]
        if 0 <= na < n and 0 <= nb < m:
            if check[na][nb]:
                return False
    return True


def backtracking(cnt, val):
    global ans

    if cnt == k:
        ans = max(val, ans)
        return

    for i in range(n):
        for j in range(m):
            if not check[i][j] and possible(i, j):
                check[i][j] = 1
                backtracking(cnt + 1, val + board[i][j])
                check[i][j] = 0

backtracking(0, 0)

print(ans)