"""
행운의 문자열
문제: https://www.acmicpc.net/problem/1342
"""
import sys, math
from collections import Counter

input = sys.stdin.readline

s = list(input().rstrip())

n = len(s)

if n == len(Counter(s)):
    print(math.factorial(n))
    sys.exit(0)

res = Counter()

tmp = []

check = [0] * n

def backtracking(level):
    if level == n:
        if "".join(tmp) not in res:
            res["".join(tmp)] += 1
        return

    for i in range(n):
        if not check[i]:
            if level >= 1:
                if s[i] == tmp[-1]:
                    continue
            check[i] = 1
            tmp.append(s[i])
            backtracking(level + 1)
            tmp.pop()
            check[i] = 0



backtracking(0)

print(len(res))