"""
이상한 술집
문제: https://www.acmicpc.net/problem/13702
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [int(input()) for _ in range(n)]

left, right = 1, max(nums)

ans = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 0

    for i in range(n):
        cnt += nums[i] // mid

    if cnt < k:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)