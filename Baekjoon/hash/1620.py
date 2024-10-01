"""
나는야 포켓몬 마스터 이다솜
문제: https://www.acmicpc.net/problem/1620
"""
import sys
from collections import Counter

input = sys.stdin.readline

name, number = Counter(), Counter()

n, m = map(int, input().split())

for i in range(n):
    s = input().rstrip()
    name[s] = i + 1
    number[i+1] = s

for _ in range(m):
    p = input().rstrip()

    if p.isdigit():
        print(number[int(p)])
    else:
        print(name[p])