"""
Moo 게임
문제: https://www.acmicpc.net/problem/5904
"""
import sys

s = "moo"

n = int(input())

# def recur(cnt):
#     if cnt == 0:
#         return s
#     return recur(cnt-1) + "m" + "o" * (cnt+2) + recur(cnt-1)

num, order = 3, 0

while n > num:
    n += 1
    num = num * 2 + order + 3


def recur(num, cur, n):
    pre = (num - cur) // 2

    if n <= pre:
        return recur(pre, cur - 1, n)
    elif n > pre:
        return recur(pre, cur - 1, n - pre - cur)
    else:
        return "o" if n-pre-1 else "m"
