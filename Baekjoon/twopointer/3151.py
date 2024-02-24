"""
합이 0
문제: https://www.acmicpc.net/problem/3151
"""
import sys
from bisect import bisect_left
from collections import Counter

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

# 각 수가 몇 개있는지 딕셔너리에 넣어줌.
dic = Counter(nums)

cnt = 0

for i in range(n-2):
    left, right = i + 1, n - 1
    while left < right:
        tmp_sum = nums[i] + nums[left] + nums[right]
        if tmp_sum < 0:
            left += 1
        elif tmp_sum > 0:
            right -= 1
        else: # 같은 경우
            if nums[left] == nums[right]: # 가르키는 곳이 같은 경우
                cnt += (right - left)
            else: # left, right의 수가 다른 경우
                cnt += dic[nums[right]]
                # tmp_idx = bisect_left(nums, nums[right])
                # cnt += right - tmp_idx + 1
            left += 1



print(cnt)

