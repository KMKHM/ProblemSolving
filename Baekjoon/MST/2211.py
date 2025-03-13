"""
네트워크 복구
문제: https://www.acmicpc.net/problem/2211
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
    if a == b:
        return
    parent[max(a, b)] = min(a, b)

edge = [list(map(int, input().split())) for _ in range(m)]

edge.sort(key=lambda x: x[2])

result, cnt = [], 0

for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        result.append((a, b))
        if sum(parent) == n:
            break

print(len(result))

for a, b in result:
    print(a, b)