"""
평범한 배낭2
문제: https://www.acmicpc.net/problem/12920
"""
import sys

input = sys.stdin.readline

n, m = map(int, input())

dp = [0] * (m+1)

for i in range(n):
    v, c, k = map(int, input().split())
    for j in range(m, v-1, -1):
        max_val1 = dp[j]
        max_val2 = 0
