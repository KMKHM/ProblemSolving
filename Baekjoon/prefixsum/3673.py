"""
나눌 수 있는 부분 수열
문제: https://www.acmicpc.net/problem/3673
"""
import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    d, n = map(int, input().split())

    nums = list(map(int, input().split()))

    prefix = [0] * n
    prefix[0] = nums[0]
    ans = 1 if nums[0] % d == 0 else 0

    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]
        ans += 1 if nums[i] % d == 0 else 0
        ans += 1 if prefix[i] % d == 0 else 0


