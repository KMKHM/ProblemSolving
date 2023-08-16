"""
N과 M (2)
문제: https://www.acmicpc.net/problem/15650
"""
n, m = map(int, input().split())

res = []

def dfs(idx):
    if len(res) == m:
       print(*res)

    for i in range(idx, n+1):
        if i not in res:
            res.append(i)
            dfs(i+1)
            res.pop()


dfs(1)
