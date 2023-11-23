"""
오르막수
문제: https://www.acmicpc.net/problem/11057
"""
n = int(input())


dp = [[1] * 11 for _ in range(n+1)]
for i in range(n):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, 11):
        dp[i][j] = sum(dp[i-1][j:])

print(dp[n][1]%10007)