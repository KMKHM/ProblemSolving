"""
구간 나누기
문제: https://www.acmicpc.net/problem/2228
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]

print(sum(nums))