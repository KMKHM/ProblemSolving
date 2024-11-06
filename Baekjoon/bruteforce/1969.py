"""
DNA
문제: https://www.acmicpc.net/problem/1969
"""
import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

s=""

arr=[input().rstrip() for _ in range(n)]

res=0

for i in range(m):
    tmp = sorted(Counter([e[i] for e in arr]).items(), key=lambda x: (-x[1], x[0]))
    s+=tmp[0][0]
    res+=sum(j for i, j in tmp[1:])
print(s)
print(res)