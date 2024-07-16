"""
끝나지 않는 파티
문제: https://www.acmicpc.net/problem/11265
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# board[i][j] = i에서 j까지 가는데 걸리는 시간
board = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

for _ in range(m):
    a, b, c = map(int, input().split())
    print("Enjoy other party" if board[a-1][b-1] <= c else "Stay here")
