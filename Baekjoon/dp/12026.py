"""
BOJ 거리
문제: https://www.acmicpc.net/problem/12026
"""
import sys

input = sys.stdin.readline

n = int(input())

s = input().rstrip()

ans = 0

dp = [sys.maxsize] * n
# 시작칸은 무조건 0
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if s[j] == "B":
            if s[i] != "O":
                continue
        if s[j] == "O":
            if s[i] != "J":
                continue
        if s[j] == "J":
            if s[i] != "B":
                continue

        dp[i] = min(dp[i], dp[j] + (i-j) ** 2)

if dp[n-1] != sys.maxsize:
    print(dp[n-1])
else:
    print(-1)



