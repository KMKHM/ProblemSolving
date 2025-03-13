"""
N과 M (1)
문제: https://www.acmicpc.net/problem/15649
"""
n, m = map(int, input().split())

def backtracking(level, arr, check):
    if level == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if not check[i]:
            arr.append(i)
            check[i] = 1
            backtracking(level+1, arr, check)
            arr.pop()
            check[i] = 0

backtracking(0, [], [0] * (n+1))