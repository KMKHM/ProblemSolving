"""
새끼치기
https://www.acmicpc.net/problem/17291
"""
import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit(0)

nums = [0] * 21
repli = [0] * 21
repli[1] = 1
repli[2] = 1
repli[3] = 2
repli[4] = 4

nums[1] = 1
nums[2] = 2
nums[3] = 4
nums[4] = 7

for i in range(5, 21):
    if i % 2 == 0:
        nums[i] = nums[i-1] * 2 - repli[i-3] - repli[i-4]
    else:
        nums[i] = nums[i-1] * 2
    repli[i] = nums[i - 1]

print(nums[n])
