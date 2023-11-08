"""
왕복
문제: https://www.acmicpc.net/problem/18311
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

distance = list(map(int, input().split()))

circuit = distance + distance[::-1]

for i in range(len(circuit)):
    k -= circuit[i]
    if k < 0:
        if i > n:
            print(len(circuit) - i)
            break
        else:
            print(i+1)
            break