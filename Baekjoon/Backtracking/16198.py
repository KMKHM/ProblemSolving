"""
에너지 모으기
문제: https://www.acmicpc.net/problem/16198
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

ans = 0
def bt(val):
    global ans

    if len(nums) == 2:
        ans = max(val, ans)
        return

    for i in range(1, len(nums)-1):
        weight = nums[i-1] * nums[i+1]
        removed = nums.pop(i)
        bt(val + weight)
        nums.insert(i, removed)


bt(0)

print(ans)