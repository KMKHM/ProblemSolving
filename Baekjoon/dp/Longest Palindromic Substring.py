"""
문제: https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=dynamic-programming
"""

s = "babad"


n = len(s)

dp = [[False]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i] == s[j]: # 만약 같은 글자가 나온다면
            if j == i-1 or dp[i+1][j-1]:
                dp[i][j] = True

