"""
정수 삼각형
문제: https://www.acmicpc.net/problem/1932
"""
import sys

input = sys.stdin.readline

n = int(input())

t = list()

for _ in range(n):
    t.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(t[i])):
        if j == 0:
            t[i][j] += t[i-1][j]
        elif j == len(t[i]) - 1:
            t[i][j] += t[i-1][j-1]
        else:
            t[i][j] += max(t[i-1][j-1], t[i-1][j])

print(max(t[n-1]))