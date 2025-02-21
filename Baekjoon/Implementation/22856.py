"""
트리 순회
문제: https://www.acmicpc.net/problem/22856
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if b != -1:
        tree[a].append(b)
    if c != -1:
        tree[a].append(c)

check = [0] * (n+1)

cnt = 0
def dfs(start):
    global cnt

    check[start] = 1

    for v in tree[start]:
        if not check[v]:
            cnt += 1
            check[start] = 1
            dfs(v)

dfs(1)

print((cnt - 1) * 2 if cnt else 0)