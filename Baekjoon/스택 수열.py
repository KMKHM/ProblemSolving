"""
https://www.acmicpc.net/problem/1874
"""
import sys

input = sys.stdin.readline

n = int(input())
stack = [i for i in range(1, n+1)]
nums = []

for _ in range(n):
    nums.append(int(input()))

print(stack)
print(nums)

