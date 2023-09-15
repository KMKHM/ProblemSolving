"""
애너그램
문제: https://www.acmicpc.net/problem/6443
"""
import sysㅌ
from collections import Counter

input = sys.stdin.readline

n = int(input())

def bt(level):
    if level == len(s):
        word["".join(res)] += 1
        return

    for i in visited:
        if visited[i]:
            res.append(i)
            visited[i] -= 1
            bt(level+1)
            visited[i] += 1
            res.pop()

for _ in range(n):
    s = sorted(input().rstrip())
    res = []
    visited = Counter()

    for i in s:
        visited[i] += 1

    word = Counter()
    bt(0)

    for a in word.keys():
        print(a)
