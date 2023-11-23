"""
기타리스트
문제: https://www.acmicpc.net/problem/1495
"""
import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())

volume = list(map(int, input().split()))

answer = -1

dp = [[0] * (m+1) for _ in range(n+1)]

# s는 무조건 1로 체크
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j + volume[i] <= m:
                dp[i+1][j+volume[i]] = 1
            if j - volume[i] >= 0:
                dp[i+1][j-volume[i]] = 1


for i in range(m+1):
    if dp[n][i] == 1:
        answer = i

print(answer)

