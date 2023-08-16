"""
이동하기
문제: https://www.acmicpc.net/problem/11048
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            board[i][j] += board[i][j-1]
        elif j == 0:
            board[i][j] += board[i-1][j]
        else:
            board[i][j] += max(board[i][j-1], board[i-1][j], board[i-1][j-1])

print(board[n-1][m-1])