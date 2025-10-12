"""
https://www.acmicpc.net/problem/1309
"""
n = int(input())

dp = [0] * (n+1)
dp[1] = 3

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + (2**i)) % 9901

print(dp[n])