"""
짝수 팰린드롬
문제: https://www.acmicpc.net/problem/21925
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n-1):
    if nums[i] == nums[i + 1]:
        dp[0][i+1] = 1

for i in dp:
    print(*i)