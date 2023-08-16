"""
N과 M (3)
문제: https://www.acmicpc.net/problem/15651
"""
n, m = map(int, input().split())

res = []

def dfs(level):

    if level == m:
        print(*res)
        return

    for i in range(1, n+1):
        res.append(i)
        dfs(level+1)
        res.pop()

dfs(0)
