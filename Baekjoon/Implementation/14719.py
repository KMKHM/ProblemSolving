"""
빗물
문제: https://www.acmicpc.net/problem/14719
"""
import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())

nums = deque(map(int, input().split()))

rain = []

# 먼저 리스트에 각 인덱스마다 최대 높이 기록
left = 0
for h in nums:
    left = max(left, h)
    rain += [left]

# for i in range(w):
#     print(rain[w-i-1], nums[w-i-1])


# 거꾸로 탐색하면서 높이 비교하며 정답 갱
right = 0
for i in range(w-1, -1, -1):
    right = max(right, nums[i])
    rain[i] = min(rain[i], right) - nums[i]

# print(rain)
print(sum(rain))

