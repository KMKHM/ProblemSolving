"""
풍선 터뜨리기
문제: https://www.acmicpc.net/problem/2346
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))


if n==1:
    print(1)
    sys.exit(0)

q = [[i+1, j] for i, j in enumerate(nums)]

cur=0

res=[]

while q:
    idx, val = q.pop(cur)
    print(q)
    res.append(idx)
    cur += (val)

    print(cur)

print(res)