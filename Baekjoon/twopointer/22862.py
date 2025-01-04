"""
가장 긴 짝수 연속한 부분 수열 (large)
문제: https://www.acmicpc.net/problem/22862
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

l, r = 0, 1
res=0
cnt=0

while l < n and r < n:
    if nums[l] % 2 == 1 and nums[r] % 2 == 0:
        r += 1
        l += 1
    elif nums[l] % 2 == 0 and nums[r] % 2 == 1:
        r += 1
        cnt += 1
    elif nums[l] % 2 == 0 and nums[r] % 2 == 0:
        if cnt <= k:
            pass
