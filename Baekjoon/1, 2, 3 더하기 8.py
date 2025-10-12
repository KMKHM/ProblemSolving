"""
문제: https://www.acmicpc.net/problem/15993
"""
import sys

input = sys.stdin.readline

mod = 1_000_000_009
dp1, dp2 = [0] * 100001, [0] * 100001
dp1[1] = 1
dp1[2] = 1
dp1[3] = 2

dp2[2] = 1
dp2[3] = 2

for i in range(4, 100001):
    dp1[i] = (dp2[i-1] + dp2[i-2] + dp2[i-3]) % mod
    dp2[i] = (dp1[i-1] + dp1[i-2] + dp1[i-3]) % mod

for _ in range(int(input())):
    n = int(input())
    print(dp1[n], dp2[n])