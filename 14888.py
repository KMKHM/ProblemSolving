import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

op = list(map(int, input().split()))

res = []

def dfs(L, value):
    if L == n:
        res.append(value)

    for i in range(4):
        dfs