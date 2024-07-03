"""
팀 빌딩
문제: https://www.acmicpc.net/problem/22945
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

ans = 0

left, right = 0, n - 1

while left + 1 < right:
    score = min(nums[left], nums[right]) * (right - left - 1)
    ans = max(ans, score)

    if nums[left] < nums[right]:
        left += 1
    else:
        right -= 1

print(ans)