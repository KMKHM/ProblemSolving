"""
동전
문제: https://www.acmicpc.net/problem/9084
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())
    dp = [0] * (k+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[k])