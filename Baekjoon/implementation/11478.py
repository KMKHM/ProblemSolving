"""
서로 다른 부분 문자열의 개수
https://www.acmicpc.net/problem/11478
"""
from collections import Counter

s = input().rstrip()

n = len(s)

res = Counter()

for i in range(n):
    for j in range(i+1, n+1):
        res[s[i:j]] += 1

print(len(res))