"""
사냥꾼
문제: https://www.acmicpc.net/problem/8983
"""
import sys, bisect

input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리
m, n, l = map(int, input().split())

# 사대의 위치
nums = list(map(int, input().split()))

nums.sort()

cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    if y > l:
        continue

    left, right = 0, m-1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] < x+y-l: # 최소값보다 작으면
            left = mid + 1
        elif nums[mid] > x-y+l: # 최대값보다 크면
            right = mid - 1
        else:
            cnt += 1
            break

print(cnt)
