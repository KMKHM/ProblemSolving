"""
회문
문제: https://www.acmicpc.net/problem/17609
"""
import sys

input = sys.stdin.readline

n = int(input())

def check(s):
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else: # 다른 경우
            if start + 1 == end:
                return 1
            if start < end - 1:
                tmp = s[:end] + s[end+1:]
                if tmp[:] == tmp[::-1]:
                    return 1
            if start + 1 < end:
                tmp = s[:start] + s[start+1:]
                if tmp[:] == tmp[::-1]:
                    return 1
            return 2
    return 0

for i in range(n):
    print(check(input().rstrip()))
