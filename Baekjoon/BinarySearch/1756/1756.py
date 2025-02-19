"""
피자 굽기
문제: https://www.acmicpc.net/problem/1756
"""
import sys

input = sys.stdin.readline

d, n = map(int, input().split())

# 오븐의 지름
nums = list(map(int, input().split()))

for i in range(d-1):
    if nums[i] < nums[i+1]:
        nums[i+1] = nums[i]

# 반죽의 지름
pizza = list(map(int, input().split()))

pizza_idx = 0
idx = d - 1

while idx >= 0:
    if pizza[pizza_idx] <= nums[idx]:
        pizza_idx += 1
        if pizza_idx == n:
            break
    idx -= 1

if pizza_idx < n:
    print(0)
else:
    print(idx+1)