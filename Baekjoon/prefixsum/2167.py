"""
2차원 배열의 합
문제: https://www.acmicpc.net/problem/2167
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

prefix = [[0] * (m+1) for _ in range(n+1)]
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + nums[i-1][j-1]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(prefix[x][y] - prefix[x][j-1] - prefix[i-1][y] + prefix[i-1][j-1])

