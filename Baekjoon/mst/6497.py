"""
전력난
문제: https://www.acmicpc.net/problem/6497
"""
import sys

input = sys.stdin.readline

def find(x, parent):
    if parent[x] == x:
        return x
    return find(parent[x], parent)

def union(a, b):
    a, b = find(a, parent), find(b, parent)

    if a == b:
        return

    parent[max(a, b)] = min(a, b)

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        sys.exit(0)

    parent = [i for i in range(n)]

    edge = [list(map(int, input().split())) for _ in range(m)]

    edge.sort(key=lambda x: x[2])

    ans = 0

    entire = 0
    for a, b, c in edge:
        entire += c
        if find(a, parent) != find(b, parent):
            union(a, b)
            ans += c

    print(entire - ans)