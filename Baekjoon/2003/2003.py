"""
수들의 합2
"""
import sys

n, m = map(int, input().split())

nums = list(map(int, input().split()))

left, right = 0, 1

res = 0

value = nums[left]

while True:
    if value < m:
        if right < n:
            value += nums[right]
            right += 1
        else:
            print(res)
            sys.exit(0)
    elif value > m:
        value -= nums[left]
        left += 1
    else:
        value -= nums[left]
        left += 1
        res += 1
