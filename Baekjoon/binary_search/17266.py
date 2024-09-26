"""
어두운 굴다리
문제: https://www.acmicpc.net/problem/17266
"""
import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

nums = list(map(int, input().split()))

res = max(nums[0], n-nums[-1])

for i in range(m-1):
    c = nums[i+1] - nums[i]
    res = max(res, c//2if c % 2 == 0 else c//2 + 1)

print(res)