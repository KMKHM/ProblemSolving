"""
전기가 부족해
문제: https://www.acmicpc.net/problem/10423
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

elec = list(map(int, input().split()))

edges = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n+1)]

visited = [0] * (n+1)

for i in elec:
    visited[i] = 1

def find(x):
    if x in elec:
        return x
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return

    if a in elec and b in elec:
        return
    elif a in elec:
        parent[b] = a
    elif b in elec:
        parent[a] = b
    else:
        parent[max(a, b)] = min(a,b)

edges.sort(key=lambda x: x[2])

result = 0

for a, b, c in edges:
    a, b = find(a), find(b)
    if a in elec and b in elec:
        continue
    if find(a) != find(b):
        union(a, b)
        result += c


print(result)
