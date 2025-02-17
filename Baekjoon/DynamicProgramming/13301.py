"""
타일 장식물
문제: https://www.acmicpc.net/problem/13301
"""
n = int(input())

dp = [0] * 81
dp[1] = dp[2] = 1

for i in range(3, 81):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] * 2 + (dp[n] + dp[n-1]) * 2)