"""
꿀 따기
문제: https://www.acmicpc.net/problem/21758
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

prefix = [0] * n

prefix[0] = nums[0]

res = 0

for i in range(1, n):
    prefix[i] = prefix[i-1] + nums[i]


# 꿀통이 가장 왼쪽에 위치한 경우
for i in range(1, n-1):
    res = max(res, prefix[n-2] - nums[i] + prefix[i-1])

# 꿀통이 가장 오른쪽에 위치한 경우
for i in range(1, n-1):
    res = max(res, prefix[n-1] - nums[0] - nums[i] + prefix[n-1] - prefix[i])


# 꿀통이 가운데 쯤 위치한 경우
for i in range(1, n-1):
    res = max(res, prefix[n-2] - nums[0] + nums[i])

print(res)