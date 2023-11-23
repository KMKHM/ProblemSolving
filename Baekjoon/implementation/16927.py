"""
배열 돌리기 2
문제: https://www.acmicpc.net/problem/16927
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 돌려야 하는 횟수
cnt = min(n, m) // 2

def rotatePart(diagonal):
    x = y = diagonal
    tmp = board[x][y]

    # 왼쪽
    for left in range(diagonal + 1, n - diagonal):
        x = left
        val = board[x][y]
        board[x][y] = tmp
        tmp = val

    # 아래쪽
    for down in range(diagonal + 1, m - diagonal):
        y = down
        val = board[x][y]
        board[x][y] = tmp
        tmp = val

    # 오른쪽
    for right in range(diagonal + 1, n - diagonal):
        x = n - right - 1
        val = board[x][y]
        board[x][y] = tmp
        tmp = val

    # 위쪽
    for up in range(diagonal + 1, m - diagonal):
        y = m - up - 1
        val = board[x][y]
        board[x][y] = tmp
        tmp = val


# 바깥쪽 = 2*(n-1) + 2*(m-1) 원상복귀
# 안쪽 => 바깥쪽과 차이가 무조건 8이다.

cycle = 2 * (n-1) + 2 * (m-1)


for k in range(cnt):
    t = r % (cycle-8*k)
    for _ in range(t):
        rotatePart(k)

for i in range(n):
    print(*board[i])