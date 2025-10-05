"""
https://www.acmicpc.net/problem/17503
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())
dic = defaultdict(list)
arr = [list(map(int, input().split())) for _ in range(k)]
for a, b in arr:
    dic[a].append(b)
for k, v in dic.items():
    v.sort()

print(dic)





