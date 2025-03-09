"""
개똥벌레
문제: https://www.acmicpc.net/problem/3020
"""
import sys

input = sys.stdin.readline

n, h = map(int, input().split())

nums = [int(input()) for _ in range(n)]

# 석순
down = sorted([nums[i] for i in range(n) if i % 2 == 0])
# 종유석
up = sorted([nums[i] for i in range(n) if i % 2 == 1])

