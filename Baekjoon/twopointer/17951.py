"""
흩날리는 시험지 속에서 내 평점이 느껴진거야
문제: https://www.acmicpc.net/problem/17951
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

start, end = 0, sum(nums)

ans = 0

while start <= end:
    mid = (start + end) // 2
    part_sum, group = 0, 0

    for score in nums:
        part_sum += score
        if part_sum >= mid:
            part_sum = 0
            group += 1

    if group >= k:
        ans = mid
        start = mid + 1
    elif group < k:
        end = mid - 1

print(ans)