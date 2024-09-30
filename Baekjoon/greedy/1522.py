"""
문자열 교환
문제: https://www.acmicpc.net/problem/1522
"""
import sys

s = input().rstrip()

if 'b' not in s:
    print(0)
    sys.exit(0)


cnt, cur = 0, ""

for i in range(len(s)):
    if s[i] == "b":
        cur = cur + "b"
    else:
        cur = ""
