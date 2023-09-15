"""
ATM
문제: https://www.acmicpc.net/problem/11399
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

ans = 0
tmp = 0
for i in range(n):
    tmp += nums[i]
    ans += tmp

print(ans)