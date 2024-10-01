"""
패션왕 신해빈
문제: https://www.acmicpc.net/problem/9375
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = defaultdict(list)

    for _ in range(n):
        k, v = input().split()
        dic[v].append(k)

    res = 1
    for k, v in dic.items():
        res *= len(v) + 1
    print(res - 1)