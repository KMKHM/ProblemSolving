"""
https://www.acmicpc.net/problem/5582
"""
s, t = input().rstrip(), input().rstrip()

s1, s2 = " "+s, " "+ t

n, m = len(s1)-1, len(s2)-1

dp = [[0]*(m+1) for _ in range(n+1)]

res = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            res = max(res, dp[i][j])
print(res)