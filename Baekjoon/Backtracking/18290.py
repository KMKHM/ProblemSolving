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


def backtracking(x, y, cnt, val):
    global ans

    if cnt == k:
        ans = max(val, ans)
        return
    # 오른쪽과 아래쪽으로만 탐색하게 된다.
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if check[i][j]:
                continue
            if not possible(i, j):
                continue
            check[i][j] = 1
            backtracking(i, j, cnt + 1, val + board[i][j])
            check[i][j] = 0

backtracking(0, 0, 0, 0)

print(ans)