"""
수학점 호기심
문제: https://www.acmicpc.net/problem/9094
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(2, n):
        for j in range(1, i):
            if ((i**2 + j**2) + m) % (i*j) == 0:
                cnt += 1
    print(cnt)