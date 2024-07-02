"""
수 나누기 게임
문제: https://www.acmicpc.net/problem/27172
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

ans = {}

for i in range(n):
    ans[nums[i]] = 0

arr = sorted(nums)

max_val = arr[-1]

for i in range(n):
    num = arr[i]
    for j in range(num*2, max_val+1, num):
        if j in ans:
            ans[num] += 1
            ans[j] -= 1

for num in nums:
    print(ans[num], end=" ")