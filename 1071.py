"""
소트
문제: https://www.acmicpc.net/problem/1071
"""
import sys
from collections import deque, Counter

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dic = Counter(nums)
q = deque()

for num in nums:
    if not dic[num]:
        continue
    if not q:
        for _ in range(dic[num]):
            q.append(num)
            dic[num] -= 1
    else:
        if q[-1] + 1 == num:
            for _ in range(dic[num]):
                q.appendleft(num)
                dic[num] -= 1
        else:
            for _ in range(dic[num]):
                q.append(num)
                dic[num] -= 1
print(*q)