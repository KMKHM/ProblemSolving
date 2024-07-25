"""
도시 건설
문제: https://www.acmicpc.net/problem/21924
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

edges = []

ans = 0

for _ in range(m):
    u, v, c = map(int, input().split())
    edges.append([u, v, c])
    ans += c

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

edges.sort(key=lambda x: x[2])

total = 0

for u, v, c in edges:
    if find(u) != find(v):
        total += c
        union(u, v)

flag = False

for i in range(2, n+1):
    if parent[i] == i:
        flag = True
        break

if flag:
    print(-1)
else:
    print(ans - total)
