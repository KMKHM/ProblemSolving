"""
리조트
문제: https://www.acmicpc.net/problem/13302
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

impossible = list(map(int, input().split()))

ticket = [1, 3, 5]

dic = {1: 10_000, 3: 25_000, 5: 50_000}

dp = [[sys.maxsize, 0] for _ in range(n+1)]
dp[0][0] = 0

for i in ticket:
    for j in range(n+1):
        if j - i >= 0 and j not in impossible:
            dp[j][0] = min(dp[j][0], dp[j-i][0] + dic[i])
            if j != 1:
                dp[j][1] = 1 if j == 3 else 2

print(dp)