"""
알바생 강호
문제: https://www.acmicpc.net/problem/1758
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0

for i in range(n):
    tmp = nums[i] - i
    if tmp < 0:
        continue
    ans += tmp

print(ans)