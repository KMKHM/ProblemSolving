"""
안녕
문제: https://www.acmicpc.net/problem/1535
"""
import sys

input = sys.stdin.readline

n = int(input())

weight = [0] + list(map(int, input().split()))
value = [0] + list(map(int, input().split()))

dp = [[0] * (101) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])