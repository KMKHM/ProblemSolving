"""
부분수열의 합
문제: https://www.acmicpc.net/problem/14225
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

check = [0] * (20 * 100000)
visited = [0] * n

res = []
def backtracking(level):
    if level <= n:
        check[sum(res)] = 1

    for i in range(level, n):
        if not visited[i]:
            res.append(nums[i])
            visited[i] = 1
            backtracking(level + 1)
            visited[i] = 0
            res.pop()

backtracking(0)

for i in range(min(nums)):
    if not check[i]:
        print(i)
        sys.exit(0)
