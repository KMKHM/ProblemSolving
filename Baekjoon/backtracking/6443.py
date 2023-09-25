"""
애너그램
문제: https://www.acmicpc.net/problem/6443
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

def bt(level):
    if level == len(s):
        word["".join(res)] += 1
        return

    for i in visited:
        # 방문할 수 있다면 백트래킹
        if visited[i]:
            res.append(i)
            visited[i] -= 1
            bt(level+1)
            visited[i] += 1
            res.pop()

for _ in range(n):
    # 입력받자마자 바로 정렬
    s = sorted(input().rstrip())
    res = []

    # 방문여부를 맵으로 표시
    visited = Counter()

    for i in s:
        visited[i] += 1

    word = Counter()
    bt(0)

    for a in word.keys():
        print(a)
