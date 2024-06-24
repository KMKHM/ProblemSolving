"""
과자 나눠주기
문제: https://www.acmicpc.net/problem/16401
"""
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

nums = list(map(int, input().split()))

ans = 0

left, right = 1, max(nums)


while left <= right:
    mid = (left + right) // 2

    cnt = sum(i // mid for i in nums)

    if cnt >= m:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans if ans else 0)