"""
배열 탈출
문제: https://www.acmicpc.net/problem/11909
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dis = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 출발점
        if i == 0 and j == 0:
            continue
        if i == 0:
            tmp = 0
            if board[i][j] < board[i][j-1]:
                tmp = dis[i][j-1]
            else:
                tmp = board[i][j] - board[i][j-1] + 1
            dis[i][j] += tmp

