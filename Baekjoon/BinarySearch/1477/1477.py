"""
휴게소 세우기
문제: https://www.acmicpc.net/problem/1477
"""
import sys

input = sys.stdin.readline

n, m, l = map(int, input().split())

nums = list(map(int, input().split())) + [0, l]
nums.sort()

left, right = 1, l-1

ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > mid:
            cnt += (nums[i] - nums[i-1] - 1) // mid # 휴게소 설치

    if cnt > m: # m보다 휴게소가 많은 경우
        left = mid + 1
    else: # 같거나 적은 경우
        right = mid - 1
        ans = mid

print(ans)