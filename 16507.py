"""
문제: https://www.acmicpc.net/problem/16507
어두운 건 무서워
"""
import sys

input = sys.stdin.readline

r, c, q = map(int, input().split())

board = [[0] * c] + [[0] + list(map(int, input().split())) for _ in range(r)]
prefix = [[0] * (c+1) for _ in range(r+1)]

for i in range(r+1):
    for j in range(c+1):
        if i == 0 or j == 0:
            continue
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + board[i][j]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    result = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
    print(result // cnt)