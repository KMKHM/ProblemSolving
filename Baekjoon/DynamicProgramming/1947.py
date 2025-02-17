"""
선물
"""
n = int(input())


if n <= 3:
    print([0, 1, 2][n-1])
else:
    dp = [0] * (n + 1)
    dp[2], dp[3] = 1, 2
    mod = 1000000000
    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) * (i-1) % mod
    print(dp[n])