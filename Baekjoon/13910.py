"""
개업
문제: https://www.acmicpc.net/problem/13910
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

w = list(map(int, input().split()))

dp = [sys.maxsize] * (n+1)

ans = -1

w_sum = sum(w)

# 만약 웍의 총
# if w_sum == n:
#     print(1)
#     sys.exit(0)

for i in range(1, sum(w) + 1):
    dp[i] = 1

# for i in range(1, n+1):
#
#     for j in range(m):