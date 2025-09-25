"""
편의점 2
문제: https://www.acmicpc.net/problem/14400
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])
x = arr[n//2][0]
arr.sort(key=lambda x: x[1])
y = arr[n//2][1]

res = 0

for ls in arr:
    res += abs(ls[0] - x) + abs(ls[1] - y)

print(res)

