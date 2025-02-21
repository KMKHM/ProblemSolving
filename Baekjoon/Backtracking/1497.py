"""
기타콘서트
문제: https://www.acmicpc.net/problem/1497
"""
import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

dic = Counter()

for _ in range(n):
    name, check = input().split()
    dic[name] = check

# 정답
ans = sys.maxsize
cnt = 0

def checks(arr):
    checked = [0] * m
    for c in arr:
        for k in range(m):
            if dic[c][k] == "Y":
                checked[k] = 1
    return sum(checked)


for i in range(1, n+1):
    for e in list(combinations(list(dic.keys()), i)):
        tmp = checks(e)
        if tmp == m:
            print(i)
            sys.exit(0)

        if cnt < tmp:
            cnt = checks(e)
            ans = i

ans = ans if ans != sys.maxsize else -1

print(ans)
