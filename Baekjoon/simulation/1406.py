"""
에디터
문제: https://www.acmicpc.net/problem/1406
"""
import sys

input = sys.stdin.readline

s = input().rstrip()

cur = len(s)

for _ in range(int(input())):
    op = list(input())

    if len(op) == 1:
        if op[0] == "L":
            if cur != 0:
                cur -= 1
        elif op[0] == "B":
            if cur == 0:
                continue
            elif cur == len(s):
                cur -= 1
                s = s[:cur]
            else:
                s = s[:cur-1] + s[cur:]
        else:
            if cur != len(s):
                cur += 1
    else:

        continue