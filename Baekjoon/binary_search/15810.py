"""
풍선 공장
문제: https://www.acmicpc.net/problem/15810
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

start, end = 1, max(nums) * m

ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt = sum(mid // num for num in nums)

    if cnt < m:
        start = mid + 1
    elif cnt >= m:
        ans = mid
        end = mid - 1

print(ans)