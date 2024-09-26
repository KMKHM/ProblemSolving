"""
가희와 키워드
문제: https://www.acmicpc.net/problem/22233
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

key = dict(zip(list(input().rstrip() for _ in range(n)), [0]*n))

for _ in range(m):
    s = input().rstrip().split(",")
    for c in s:
        if c in key:
            del key[c]
    print(len(key))