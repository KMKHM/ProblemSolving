"""
회사에 있는 사람
문제: https://www.acmicpc.net/problem/7785
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

dic = Counter()

for _ in range(n):
    name, op = input().split()
    dic[name] = op

for name in sorted([i for i, j in dic.items() if j == "enter"], reverse=True):
    print(name)