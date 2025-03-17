"""
친구 네트워크
문제: https://www.acmicpc.net/problem/4195
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

t = int(input())

def find(s):
    if parent[s] == s:
        return s
    parent[s] = find(parent[s])
    return parent[s]

def union(s1, s2):
    root_s1 = find(s1)
    root_s2 = find(s2)
    if root_s1 == root_s2:
        return
    else:
        parent[root_s2] = root_s1
        check[root_s1] += check[root_s2]

for _ in range(t):

    m = int(input())

    parent, check = dict(), dict()

    for _ in range(m):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            check[a] = 1
        if b not in parent:
            parent[b] = b
            check[b] = 1

        union(a, b)
        print(check[find(a)])




