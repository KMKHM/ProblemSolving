"""
구간 합 구하기 4
문제: https://www.acmicpc.net/problem/11659
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

prefix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + nums[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])

print(nums)
print(prefix)