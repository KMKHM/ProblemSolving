"""
최소 스패닝 트리
문제: https://www.acmicpc.net/problem/1197
"""
import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edge = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

# 가중치로 정렬
edge.sort()

# 부모 테이블
parent = [i for i in range(v+1)]

# find
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union
def union(a, b):
    root_a, root_b = find(a), find(b)

    if root_a == root_b:
        return

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

answer = 0

for c, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)






