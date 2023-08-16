"""
여행 가자
문제: https://www.acmicpc.net/problem/1976
"""
import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

e = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            e.append((i+1, j+1))


# 부모 테이블
parent = [i for i in range(n+1)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return
    elif root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


nums = list(map(int, input().split()))

for a, b in e:
    union(a, b)


start = parent[nums[0]]

for i in range(1, m):
    if parent[nums[i]] != start:
        print("NO")
        sys.exit(0)
print("YES")





