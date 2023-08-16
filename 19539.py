"""
사과나무
문제: https://www.acmicpc.net/problem/19539
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

heapq.heapify(nums)

while 1:
    if not nums:
        break
    if len(nums) == 1:
        if nums[0] % 2 == 0 or nums[0] % 3 != 0:
            break
    # 3으로 나눠지면 바로 pop
    if nums[0] % 3 == 0:
        heapq.heappop(nums)

    elif nums[0] % 2 == 0:
        cnt = nums[0] // 2
        heapq.heappop(nums)
        nums[0] -= cnt
    else:
        t = heapq.heappop(nums)
        if nums[0] < 2*t:
            break



print(nums)