"""
징검다리 건너기
문제: https://www.acmicpc.net/problem/21317
"""
import sys

input = sys.stdin.readline

n = int(input())

# 작은 점프, 큰 점프
jumps = [[0, 0]] + [list(map(int, input().split())) for _ in range(n-1)]

k = int(input())

dp = [sys.maxsize] * 30
dp[0] = 0
dp[1] = 0

for i in range(1, n-2):
    dp[i+1] = min(dp[i+1], dp[i] + jumps[i][0])
    dp[i+2] = min(dp[i+2], dp[i] + jumps[i][1])
    dp[i+3] = min(dp[i+3], dp[i] + k)
print(dp[n])


