"""
서울에서 경산까지
문제: https://www.acmicpc.net/problem/14863
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# dp[i][j] = 현재 i 번째 도시에 있고, 현재까지 걸리시간이 j일 때 최대값
dp = [[0] * (100001) for _ in range(n+1)]

for i in range(1, n+1):
    # 도보시간 / 도보금액 / 자전거시간 / 자전거금액
    a, b, c, d = map(int, input().split())

    if i == 1:
        dp[i][a] = b
        dp[i][c] = max(dp[i][c], d)

    else:
        for j in range(k):
            if dp[i-1][j] == 0:
                continue
            else:
                if (j + a) <= k:
                    dp[i][j+a] = max(dp[i][j+a], dp[i-1][j]+b)
                if (j + c) <= k:
                    dp[i][j+c] = max(dp[i][j+c], dp[i-1][j]+d)

ans = 0

for i in range(1, k+1):
    ans = max(ans, dp[n][i])

print(ans)






