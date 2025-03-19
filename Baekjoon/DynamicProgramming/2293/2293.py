"""
동전 1
문제: https://www.acmicpc.net/problem/2293
"""
import sys

input = sys.stdin.readline

# 동전의 종류, 가치의 합
n, k = map(int, input().split())

# 동전
coins = [int(input()) for _ in range(n)]

# dp
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]
        print(i, coin, dp)
print(dp[k])

