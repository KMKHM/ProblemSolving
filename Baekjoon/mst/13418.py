"""
학교 탐방하기
문제: https://www.acmicpc.net/problem/13418
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 부모 테이블
parent1 = [i for i in range(n+1)]
parent2 = [i for i in range(n+1)]

# find
def find(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]

# union
def union(a, b, parent):
    a, b = find(a, parent), find(b, parent)
    if a == b:
        return
    parent[max(a, b)] = min(a, b)

max_val, min_val = 0, 0

edges1 = []
a, b, c = map(int, input().split())
edges1.append((a,b,not c))

edges2 = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges2.append((a,b,not c))

edges2.sort(key=lambda x: x[2])

# 최선의 경로
for a, b, c in edges1+edges2:
    if find(a, parent1) != find(b, parent1):
        union(a, b, parent1)
        min_val += c

# 최악의 경로
edges2.sort(reverse=True, key=lambda x: x[2])

for a, b, c in edges1+edges2:
    if find(a, parent2) != find(b, parent2):
        union(a, b, parent2)
        max_val += c



print(max_val**2 - min_val**2)