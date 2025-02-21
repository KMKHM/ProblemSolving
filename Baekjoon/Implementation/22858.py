"""
원상 복구 (small)
문제: https://www.acmicpc.net/problem/22858
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

res = list(map(int, input().split()))

d = list(map(int, input().split()))

while k:
    origin = [0] * n
    for i in range(n):
        origin[d[i]-1] = res[i]
    res = origin
    k -= 1


print(*origin)
