"""
배열 돌리기 1
문제: https://www.acmicpc.net/problem/16926
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 돌려야하는 수
cnt = min(n, m) // 2

def rotate_arr(num):
    # 초기값을 맨 처음 대각선을 설정
    x = y = num
    temp_value = board[x][y]

    # 왼쪽
    for left in range(num+1, n-num):
        x = left
        value = board[x][y]
        board[x][y] = temp_value
        temp_value = value

    # 아래쪽
    for down in range(num+1, m-num):
        y = down
        value = board[x][y]
        board[x][y] = temp_value
        temp_value = value

    # 오른쪽
    for right in range(num+1, n-num):
        x = n - right - 1
        value = board[x][y]
        board[x][y] = temp_value
        temp_value = value

    # 위쪽
    for up in range(num+1, m-num):
        y = m - up - 1
        value = board[x][y]
        board[x][y] = temp_value
        temp_value = value

for _ in range(r):
    for i in range(cnt):
        rotate_arr(i)

for a in range(n):
    print(*board[a])

