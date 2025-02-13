"""
우체국
문제: https://www.acmicpc.net/problem/2285
"""
import sys

input = sys.stdin.readline

n = int(input())

home = []

for i in range(n):
    a, b = map(int, input().split())
    home.append([a, b])

home.sort()

prefix_sum = [0] * n

prefix_sum[0] = home[0][1]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + home[i][1]


for i in range(n):
    cur = prefix_sum[i]
    left = prefix_sum[n-1] - prefix_sum[i]
    if cur >= left:
        print(home[i][0])
        sys.exit(0)