"""
군사 이동
문제: https://www.acmicpc.net/problem/11085
"""
import sys, heapq

input = sys.stdin.readline

p, w = map(int, input().split())

c, v = map(int, input().split())

parent = [i for i in range(p)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

q = []

for _ in range(w):
    a, b, w = map(int, input().split())
    heapq.heappush(q, (-w, a, b))

while q:
    w, a, b = heapq.heappop(q)
    w *= -1
    union(a, b)

    if find(c) == find(v):
        print(w)
        sys.exit(0)