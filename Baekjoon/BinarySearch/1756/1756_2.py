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


left, right = 0, d-1
dough = 0

for p in pizza:

    flag = False

    while left <= right:
        mid = (left + right) // 2
        if p <= nums[mid]:
            left = mid + 1
            dough = mid
            flag = True
        else:
            right = mid - 1

    if not flag:
        print(0)
        sys.exit(0)

    left, right = 0, dough - 1

print(dough + 1)