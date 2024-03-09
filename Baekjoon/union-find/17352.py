"""
여러분의 다리가 되어 드리겠습니다!
문제: https://www.acmicpc.net/problem/17352
"""
import sys

input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    pa, pb = find(a), find(b)

    if pa != pb:
        parent[max(pa, pb)] = min(pa, pb)


if n == 2:
    print(1, 2)
    sys.exit(0)
else:
    for _ in range(n-2):
        a, b = map(int, input().split())
        union(a, b)

tmp = []

for i in range(1, n + 1):
    parent[i] = find(i)
    if parent[i] not in tmp:
        tmp.append(parent[i])

print(tmp[0], tmp[1])