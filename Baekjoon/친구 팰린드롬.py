"""
https://www.acmicpc.net/problem/15270
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

if m == 0:
    print(1)
    sys.exit(0)

for _ in range(m):
    a, b = map(int, input().split())
    

