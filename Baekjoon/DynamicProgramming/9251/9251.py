"""
LCS
문제: https://www.acmicpc.net/problem/9251
"""
import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            continue

        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])