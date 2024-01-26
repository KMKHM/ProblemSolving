"""
귀찮아 (SIB)
문제: https://www.acmicpc.net/problem/14929
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

val = sum(nums)

ans = 0

for i in range(n-1):
    ans += (nums[i] * (val-nums[i]))
    val -= nums[i]

print(ans)