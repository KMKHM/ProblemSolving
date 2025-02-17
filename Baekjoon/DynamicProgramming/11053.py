"""
가장 긴 증가하는 부분 수열
문제: https://www.acmicpc.net/problem/11053
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n


for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))