"""
설탕 배달
문제: https://www.acmicpc.net/problem/2839
"""
n = int(input())

dp = [5000] * 5001

# 3kg, 5kg
dp[3], dp[5] = 1, 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] >= 5000:
    print(-1)
else:
    print(dp[n])







