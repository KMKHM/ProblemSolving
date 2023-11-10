"""
완전 이진 트리
문제: https://www.acmicpc.net/problem/9934
"""
import sys

input = sys.stdin.readline

k = int(input())

nums = list(map(int, input().split()))

res = [[] for _ in range(k)]

def dfs(level, arr):
    left, right = 0, len(arr) - 1
    mid = (left + right) // 2

    if level == k:
        return

    res[level].append(arr[mid])

    dfs(level + 1, arr[:mid])
    dfs(level + 1, arr[mid+1:])

dfs(0, nums)

for array in res:
    print(*array)