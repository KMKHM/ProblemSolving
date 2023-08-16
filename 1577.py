"""
도로의 개수
문제: https://www.acmicpc.net/problem/1577
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

dp = [[0] * m for _ in range(n)]

for i in range(1, n):
    dp[i][0] = 1
for j in range(1, m):
    dp[0][j] = 1

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            continue
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[-1][-1])

print(dp)