"""
균형잡힌 세상
문제: https://www.acmicpc.net/problem/4949
"""
import sys

input = sys.stdin.readline


def check(s):
    stack = []
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif c == "]":
            if not stack:
                return False
            if stack[-1] == "[":
                stack.pop()
            else:
                return False

    return len(stack) == 0

while 1:
    s = input().rstrip()

    if s == ".":
        break

    ans = "yes" if check(s) else "no"
    print(ans)