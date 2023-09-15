"""
순회강연
문제: https://www.acmicpc.net/problem/2109
"""
import sys


input = sys.stdin.readline

n = int(input())

lecture = [list(map(int, input().split())) for _ in range(n)]

# 먼저 d일 기준으로 오름차순 정렬
lecture.sort(key=lambda x: x[1])


s, e = lecture[0][1], lecture[-1][1]

dp = [0] * (e+1)

for i in range(n):
    if dp[i]:
        dp[i] = max(dp[i], lecture[i][0])
    for j in range(1, lecture[i][1]):
        if not dp[j]:
            dp[j] = lecture[i][1]
print(dp)
print(sum(dp))

