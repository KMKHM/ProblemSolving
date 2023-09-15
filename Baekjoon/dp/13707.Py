"""
합분해 2
문제: https://www.acmicpc.net/problem/13707
"""
import sys

n, k = map(int, input().split())

if n == 1:
    print(1)
    sys.exit(0)

mod = 1000000000

# dp 테이블
dp = [[0]*(n+1) for _ in range(k+1)]

# K = 1 인 경우 무조건 1가지 경우의 수
for i in range(n+1):
    dp[1][i] = 1

for i in range(1, k+1):
    dp[i][0] = 1

for i in range(2, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
        if i == k and j == n:
            print(dp[k][n])
            sys.exit(0)
