"""
문제: https://www.acmicpc.net/problem/1765
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = int(input()), int(input())

enemy = defaultdict(list)

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    x, y = find(x), find(y)
    parent[max(x, y)] = min(x, y)

for _ in range(m):
    arr = list(input().rstrip().split())
    a, b = int(arr[1]), int(arr[2])

    if arr[0] == "F":
        union(a, b)
    else:
        enemy[a].append(b)
        for e in enemy[a]:
            union(b, e)
        enemy[b].append(a)
        for e in enemy[b]:
            union(a, e)

for i in range(1, n+1):
    parent[i] = find(parent[i])

print(len(set(parent))-1)

