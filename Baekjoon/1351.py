"""
무한 수열
문제: https://www.acmicpc.net/problem/1351
"""
from collections import Counter

n, p, q = map(int, input().split())

nums = Counter()

nums[0] = 1

def recur(n):
    if n in nums:
        return nums[n]
    else:
        nums[n] = recur(n//p) + recur(n//q)
        return nums[n]

print(recur(n))
