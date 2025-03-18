"""
캠프 준비
문제: https://www.acmicpc.net/problem/16938
"""
import sys

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
nums = list(map(int, input().split()))

def backtracking(idx, total, min_val, max_val, count):

    valid_count = 0

    if count >= 2:
        if l <= total <= r and max_val - min_val >= x:
            valid_count += 1

    for i in range(idx, n):
        valid_count += backtracking(i + 1, total + nums[i], min(min_val, nums[i]), max(max_val, nums[i]), count + 1)

    return valid_count

print(backtracking(0, 0, sys.maxsize, -sys.maxsize, 0))