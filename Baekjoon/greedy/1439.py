"""
뒤집기
문제: https://www.acmicpc.net/problem/1439
"""
import sys

s = input().rstrip()

if len(s) == 1 or "1" not in s or "0" not in s:
    print(0)
    sys.exit(0)

one, zero = 0, 0

tmp = s[0]

for c in s[1:]:
    if tmp == c:
        continue
    else:
        if tmp == "1":
            one += 1
        else:
            zero += 1
        tmp = c

if tmp == "0":
    zero += 1
else:
    one += 1

print(min(one, zero))