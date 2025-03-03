"""
스크루지 민호
https://www.acmicpc.net/problem/12896
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [[sys.maxsize] * (n+1) for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, n+1):
    dp[i][i] = 0

ans = sys.maxsize

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in dp[1:]:
    ans = min(ans, max(i[1:]))

print(ans)