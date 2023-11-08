"""
RGB 거리
문제: https://www.acmicpc.net/problem/1149
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1, n):
    nums[i][0] = min(nums[i - 1][1], nums[i - 1][2]) + nums[i][0]
    nums[i][1] = min(nums[i - 1][0], nums[i - 1][2]) + nums[i][1]
    nums[i][2] = min(nums[i - 1][0], nums[i - 1][1]) + nums[i][2]


print(min(nums[n - 1][0], nums[n - 1][1], nums[n - 1][2]))