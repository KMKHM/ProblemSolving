"""
사과나무
문제: https://www.acmicpc.net/problem/20002
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + board[i-1][j-1]


ans = -sys.maxsize

for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            ans = max(prefix[i+k][j+k] - prefix[i-1][j+k] - prefix[i+k][j-1] + prefix[i-1][j-1], ans)

print(ans)