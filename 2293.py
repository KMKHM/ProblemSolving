"""
동전 1
문제: https://www.acmicpc.net/problem/2293
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)
dp[0] = 1
coins = []

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for j in range(coin, k+1):
        if j >= coin:
            dp[j] += dp[j-coin]

print(dp[-1])
