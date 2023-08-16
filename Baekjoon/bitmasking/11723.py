"""
집합의 표현
"""
import sys

input = sys.stdin.readline

s = 0

m = int(input())

for _ in range(m):
    operation = input().split()
    if len(operation) == 1:
        if operation[0] ==
    else:
        if operation[0] == "add":
            m |= (1<<int(operation[1]))
        elif operation[0] == "remove":
            m &= ~(1<<int(operation[1]))
