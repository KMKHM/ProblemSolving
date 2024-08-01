"""
인간-컴퓨터 상호작용
문제: https://www.acmicpc.net/problem/16139
"""
import sys

input = sys.stdin.readline

s = input().rstrip()

n = len(s)

cache = [[0] * 26 for _ in range(n)]

for i in range(n):
    for j in range(26):
        if (ord(s[i]) - 97) == j:
            cache[i][j] = cache[i-1][j] + 1
        else:
            cache[i][j] = cache[i-1][j]

q = int(input())

for _ in range(q):
    alpha, start, end = input().split()

    alpha, start, end = ord(alpha)-97, int(start), int(end)
    if start == 0:
        print(cache[end][alpha])
    else:
        print(cache[end][alpha] - cache[start-1][alpha])