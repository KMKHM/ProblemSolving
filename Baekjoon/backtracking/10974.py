"""
모든 순열
문제: https://www.acmicpc.net/problem/10974
"""
n = int(input())

res = []

def bt(level):
    if level == n:
        print(*res)

    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            bt(level+1)
            res.pop()
bt(0)