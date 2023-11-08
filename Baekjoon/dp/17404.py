"""
RGB 거리2
https://www.acmicpc.net/problem/17404
"""
# 1번집과 n번집의 색이 달라야함

import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
nums.insert(0, [0, 0, 0])
r, g, b = 0, 1, 2

answer = sys.maxsize

for color in [r, g, b]:
    dp = [[-1]*3 for _ in range(n+1)]
    dp[1] = [sys.maxsize, sys.maxsize, sys.maxsize]
    dp[1][color] = nums[1][color]

    for i in range(2, n+1):
        dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + nums[i][r]
        dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + nums[i][g]
        dp[i][b] = min(dp[i-1][g], dp[i-1][r]) + nums[i][b]

    dp[n][color] = sys.maxsize

    answer = min(answer, min(dp[n]))

print(answer)
