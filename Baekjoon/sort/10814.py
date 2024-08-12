"""
나이순 정렬
문제: https://www.acmicpc.net/problem/10814
"""
import sys

input = sys.stdin.readline

n = int(input())

res = []

for i in range(n):
    arr = input().split()
    res.append([int(arr[0]), arr[1], i])

res.sort(key=lambda x: (x[0], x[2]))

for i in res:
    print(*i[:2])