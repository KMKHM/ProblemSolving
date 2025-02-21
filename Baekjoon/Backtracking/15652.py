"""
N과 M (4)
문제: https://www.acmicpc.net/problem/15652
"""
n, m = map(int, input().split())

res = []

def dfs(level):
    if len(res) == m:
        print(*res)
        return

    for i in range(level, n+1):
        res.append(i)
        dfs(i)
        res.pop()

dfs(1)

