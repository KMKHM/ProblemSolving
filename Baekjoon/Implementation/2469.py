"""
사다리 타기
문제: https://www.acmicpc.net/problem/2469
"""
import sys

input = sys.stdin.readline

k = int(input())

n = int(input())

order = input().rstrip()

origin = sorted(order)

ladder = [list(input().rstrip()) for _ in range(n)]

start, end = [], []

for i in range(n):
    if ladder[i][0] == "?":
        start = ladder[:i]
        end = ladder[i+1:]
        break


for char in start:
    for i in range(k-1):
        if char[i] == "-":
            origin[i], origin[i+1] = origin[i+1], origin[i]
    print(origin)
