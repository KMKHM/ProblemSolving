"""
집합의 표현
문제: https://www.acmicpc.net/problem/1717
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())

# 부모 테이블
parent = [i for i in range(n+1)]

# find 연산
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union 연산
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y




for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")