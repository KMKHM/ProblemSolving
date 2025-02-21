"""
N과 M (1)
문제: https://www.acmicpc.net/problem/15649
"""
n, m = map(int, input().split())

res = []

def dfs(level):
    if level == m:
        print(*res)

    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            dfs(level+1)
            res.pop()

dfs(0)