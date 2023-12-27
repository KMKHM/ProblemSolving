"""
합이 0
문제: https://www.acmicpc.net/problem/3151
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()


cnt = 0

for i in range(n-2):
    left, right = i + 1, n - 1
    while left < right:
        tmp_sum = nums[i] + nums[left] + nums[right]
        if tmp_sum < 0:
            left += 1
        elif tmp_sum > 0:
            right -= 1
        else:
            left += 1
            cnt += 1

print(cnt)

