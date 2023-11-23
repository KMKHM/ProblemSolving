"""
제곱수의 합
문제: https://www.acmicpc.net/problem/1699
"""
n = int(input())

# 1 = 1 ^ 2 = 1
# 2 = 1 ^ 2 + 1^2 = 2
# 3 = 1 ^ 2 + 1^2 + 1^2 = 3

# 4 = 2 ^ 2 = 1
# 5 = 2^2 + 1^1 = 2
# 6 = 2^2 + 1^2 + 1^2 = 3
# 7 = 4

# 8 = 2
# 9 = 1
# 10 = 2 = 9 + 1
# 11 = 3 = 9 + 2
# 12 = 2^2 + 2^2 + 2^2 = 4 + 4 + 4
# 13 = 9 + 4

# 16 = 4 ^ 2 = 1
# 17 = 2
# 18 = 2
# 19 = 3

dp = [i for i in range(n+1)]


for i in range(2, n+1):
    for j in range(1, i):
        tmp = j * j

        if i < tmp:
            break

        dp[i] = min(dp[i], dp[i-tmp]+1)


print(dp[n])
