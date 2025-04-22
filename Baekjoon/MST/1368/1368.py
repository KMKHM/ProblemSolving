"""
물대기
문제: https://www.acmicpc.net/problem/1368
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

edge = []

for i in range(n):
    num = int(input())
    edge.append((num, 0, i + 1))

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if i < j:
            edge.append((nums[j], i+1, j+1))

edge.sort()

parent = [i for i in range(n+1)]

def find(x):
    return parent[x] if x == parent[x] else find(parent[x])

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

cost = 0

for c, a, b in edge:
    a, b = find(a), find(b)
    if a == b:
        continue
    union(a, b)
    print(a,b, c)
    cost += c

print(parent)
print(cost)