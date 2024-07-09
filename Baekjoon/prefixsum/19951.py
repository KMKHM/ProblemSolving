"""
태상이의 훈련소 생활
문제: https://www.acmicpc.net/problem/19951
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

check = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    check[a-1] += c
    check[b] -= c

tmp = 0

for i in range(n):
    tmp += check[i]
    print(nums[i] + tmp, end=" ")