"""
행성 탐사
문제: https://www.acmicpc.net/problem/5549
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

prefix = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]

board = [list(input().rstrip()) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j][0] = prefix[i - 1][j][0] + prefix[i][j - 1][0] - prefix[i - 1][j - 1][0]
        prefix[i][j][1] = prefix[i - 1][j][1] + prefix[i][j - 1][1] - prefix[i - 1][j - 1][1]
        prefix[i][j][2] = prefix[i - 1][j][2] + prefix[i][j - 1][2] - prefix[i - 1][j - 1][2]

        if board[i-1][j-1] == "J":
            prefix[i][j][0] += 1
        elif board[i-1][j-1] == "O":
            prefix[i][j][1] += 1
        else:
            prefix[i][j][2] += 1


for _ in range(k):
    a, b, c, d = map(int, input().split())
    res = []
    for i in range(3):
        res.append(prefix[c][d][i] - prefix[a-1][d][i] - prefix[c][b-1][i] + prefix[a-1][b-1][i])
    print(*res)