"""
카드 1
문제: https://www.acmicpc.net/problem/2161
"""
from collections import deque

nums = deque(i for i in range(1, int(input())+1))

stack = []

while len(nums) > 1:
    stack.append(nums.popleft())
    nums.append(nums.popleft())

print(*stack, nums[0])