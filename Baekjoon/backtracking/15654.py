"""
N과 M (5)
문제: https://www.acmicpc.net/problem/15654
"""
n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))

res = []

check = [0] * n

def dfs(level):
    if level == m:
        print(*res)
        return

    for i in range(n):
        if not check[i]:
            check[i] = 1
            res.append(nums[i])
            dfs(level+1)
            check[i] = 0
            res.pop()

dfs(0)