"""
적의 적
문제: https://www.acmicpc.net/problem/12893
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

enemy = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    up, vp = find(u), find(v)

    if up == vp:
        print(0)
        sys.exit(0)

    if enemy[u] != 0:
        union(enemy[u], v)
    else:
        enemy[u] = v

    if enemy[v] != 0:
        union(enemy[v], u)
    else:
        enemy[v] = u

print(1)






