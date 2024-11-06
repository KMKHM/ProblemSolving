"""
회전하는 큐
문제: https://www.acmicpc.net/problem/1021
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

nums = deque(i for i in range(1, n+1))

extract = list(map(int, input().split()))

cnt = 0

for i in range(m):
     if nums[0] == extract[i]:
         nums.popleft()
     else:
        a, b = 0, 0


print(cnt)