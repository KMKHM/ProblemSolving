"""
카드
문제: https://www.acmicpc.net/problem/11652
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

dic = Counter()

for _ in range(n):
    dic[int(input())] += 1

a = list(dic.most_common())
val = a[0][1]
ans = []
for i, j in a:
    if j == val:
        ans.append(i)
print(sorted(ans)[0])

