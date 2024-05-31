"""
암벽 등반
문제: https://www.acmicpc.net/problem/2412
"""
import sys

input = sys.stdin.readline

n, t = map(int, input().split())

board = []

flag = False

for _ in range(n):
    a, b = map(int, input().split())
    if b == t:
        flag = True
    board.append([a, b])

if not flag:
    print(-1)
    sys.exit(0)

cur = [0, 0]

def check(x, y, a, b):
    return abs(x-a) <= 2 and (y-b) <= 2

