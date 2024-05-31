"""
팰린드롬 만들기
문제: https://www.acmicpc.net/problem/1254
"""
import sys

input = sys.stdin.readline

s = input().rstrip()

if s == s[::-1]:
    print(len(s))
    sys.exit(0)

n = 0

temp = ""

while 1:
    if (s+temp) == (s+temp)[::-1]:
        break
    temp = s[n] + temp
    n += 1

print(len(s+temp))