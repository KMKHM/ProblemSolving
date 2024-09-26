"""
IF문 좀 대신 써줘
문제: https://www.acmicpc.net/problem/19637
"""
import sys, bisect

input = sys.stdin.readline

n, m = map(int, input().split())

op, c = [], []

for _ in range(n):
    a, b = input().split()
    op.append(a)
    c.append(int(b))


for _ in range(m):
    print(op[bisect.bisect_left(c, int(input()))])


