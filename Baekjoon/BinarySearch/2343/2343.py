"""
기타 레슨
문제: https://www.acmicpc.net/problem/2343
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

ans = 0

left, right = max(nums), sum(nums)

while left <= right:

    mid = (left + right) // 2

    total, cnt = 0, 1

    for num in nums:
        if total + num > mid:
            cnt += 1
            total = 0
        total += num

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)