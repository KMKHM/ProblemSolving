"""
호텔
문제: https://www.acmicpc.net/problem/1106
"""
import sys

input = sys.stdin.readline

c, n = map(int, input().split())

dp = [[sys.maxsize]*(c+1) for _ in range(n+1)]
for i in range(c+1):
    dp[0][i] = 0

values = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, n+1):

    cost, person = values[i-1][0], values[i-1][1]

    for j in range(1, c+1):

        if j < person:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - person] + cost*(j//person))



print(dp)



