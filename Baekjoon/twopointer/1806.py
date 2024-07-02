"""
부분합
문제: https://www.acmicpc.net/problem/1806
"""
import sys

input = sys.stdin.readline

n, s = map(int, input().split())

length = sys.maxsize

nums = list(map(int, input().split()))

tmp_sum = nums[0]

left, right = 0, 0

while 1:
    if tmp_sum < s:
        right += 1
        if right == n:
            break
        tmp_sum += nums[right]
    else:
        tmp_sum -= nums[left]
        length = min(length, right - left + 1)
        left += 1

print(length if length != sys.maxsize else 0)