"""
불우이웃돕기
문제: https://www.acmicpc.net/problem/1414
"""
import sys

input = sys.stdin.readline

n = int(input())

edges = []

res = 0

for i in range(n):
    s = input().rstrip()
    arr = []
    for j in range(n):
        if s[j].isupper():
            arr.append(ord(s[j]) - ord("A") + 27)
        elif s[j].islower():
            arr.append(ord(s[j]) - ord("a") + 1)
        else:
            arr.append(int(s[j]))

        if i != j and arr[j] != 0:
            edges.append((arr[j], i, j))
    res += sum(arr)


parent = [0] * n

for i in range(n):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

edges.sort()

for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res -= c

for i in range(n):
    parent[i]=find(i)
    if parent[i] != 0:
        print(-1)
        sys.exit(0)

print(res)