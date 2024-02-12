"""
파닭파닭
문제: https://www.acmicpc.net/problem/14627
"""
import sys

input = sys.stdin.readline

s, c = map(int, input().split())

nums = [int(input()) for _ in range(s)]

left, right = 1, max(nums)

ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for num in nums:
        cnt += (num // mid)

    if cnt >= c:
        ans = mid
        left = mid + 1
    elif cnt < c:
        right = mid - 1

print(sum(nums) - c*ans)