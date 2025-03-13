"""
나만 안되는 연애
문제: https://www.acmicpc.net/problem/14621
"""
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

school = list(input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)
    # if a==b:
    #     return
    parent[max(a, b)] = min(a, b)

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

ans = 0

for a, b, c in edges:

    if school[a-1] != school[b-1]:
        if find(a) != find(b):
            union(a, b)
            ans += c

for i in parent[1:]:
    i = find(i)
    if i != 1:
        print(-1)
        sys.exit(0)

print(ans)