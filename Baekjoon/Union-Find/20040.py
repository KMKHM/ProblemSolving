"""
사이클 게임
문제: https://www.acmicpc.net/problem/20040
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return

    parent[max(a, b)] = min(a, b)

def check(a, b):
    return find(a) == find(b)


for i in range(1, m+1):
    a, b = map(int, input().split())
    if check(a, b):
        print(i)
        sys.exit(0)
    union(a, b)

print(0)