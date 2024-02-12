"""
합 구하기
문제: https://www.acmicpc.net/problem/11441
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

prefix_sum = [0] * n

val = 0

for i in range(n):
    val += nums[i]
    prefix_sum[i] = val

prefix_sum = [0] + prefix_sum


m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])

