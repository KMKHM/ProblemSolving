"""
회전초밥
문제: https://www.acmicpc.net/problem/2531
"""
import sys

input = sys.stdin.readline

# 접시수, 가짓수, 연속해서 먹은 접시수, 쿠폰 번호
n, d, k, c = map(int, input().split())

nums = [int(input()) for _ in range(n)]

flag = False

if c in nums:
    flag = True

nums += nums[:k]

ans = 0

for i in range(n):
    tmp = set(nums[i:i+k])

    if flag: # 쿠폰O
        length = len(tmp) if c in tmp else len(tmp) + 1
        ans = max(ans, length)
    else: # 쿠폰X
        ans = max(ans, len(tmp)+1)

print(ans)