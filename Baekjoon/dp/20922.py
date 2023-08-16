"""
겹치는 건 싫어
문제: https://www.acmicpc.net/problem/20922
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

dp = [0] * n

dp[0] = 1

dic = dict()
dic[nums[0]] = 1


for i in range(1, n):
    if nums[i] not in dic:
        dic[nums[i]] = 1
        dp[i] = dp[i-1]

    if dic[nums[i]] <= k:
        dic[nums[i]] += 1
        dp[i] = dp[i-1] + 1

    else:
        dp[i] = dp[i-1]

print(dp)

