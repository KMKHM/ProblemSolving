"""
가장 긴 짝수 연속한 부분 수열 (small)
문제: https://www.acmicpc.net/problem/22857
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

ans = 0

flag = False

for i in range(1, n):
    for j in range(i, n+1):
        # print(j-i+1) 배열의 길이
        if i == j:
            if nums[i] % 2 == 0:
                dp[i][j] = 1
                flag = True
                continue
        if nums[j] % 2 == 0:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i][j-1]

        if dp[i][j]:
            length = j - i + 1


