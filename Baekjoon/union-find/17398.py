"""
통신망 분할
문제: https://www.acmicpc.net/problem/17398
"""
import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

parent = [i for i in range(n+1)]
size = [1] * (n+1)
ans = 0

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return 0

    a_size, b_size = size[a], size[b]
    parent[max(a, b)] = min(a, b)
    size[min(a, b)] += size[max(a, b)]
    size[max(a, b)] = 0

    return a_size * b_size

connect = [[0, 0]]

for _ in range(m):
    a, b = map(int, input().split())
    connect.append([a, b])

visited = [0] * (m+1)

query = []

for _ in range(q):
    c = int(input())
    query.append(c)
    visited[c] = 1

for i in range(1, m+1):
    if not visited[i]:
        union(connect[i][0], connect[i][1])

for q in query[::-1]:
    a, b = connect[q]
    ans += union(a, b)

print(ans)