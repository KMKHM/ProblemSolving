"""
롤케이크
문제: https://www.acmicpc.net/problem/16206
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

result = []

for num in nums:
    slice_count, res = 0, 0
    if num <= 10:
        slice_count = 0
        if num < 10:
            res = 0
        else:
            res = 1
    else:
        if num % 10 == 0:
            slice_count = num // 10 - 1
        else:
            slice_count = num // 10
        res = num // 10
    result.append([slice_count, res])

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    # weight, value
    cnt, res = result[i-1]
    for j in range(1, m+1):
        if cnt > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cnt] + res)

print(dp)




