"""
소셜 네트워킹 어플리케이션
문제: https://www.acmicpc.net/problem/7511
"""
import sys

input = sys.stdin.readline

t = int(input())

def find(x, parent):
    if parent[x] == x:
        return x
    return find(parent[x], parent)

def union(a, b, parent):
    a, b = find(a, parent), find(b, parent)

    if a == b:
        return

    parent[max(a, b)] = min(a, b)


for i in range(t):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n+1)]

    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b, parent)

    print("Scenario " + str(i+1) + ":")
    c = int(input())
    for _ in range(c):
        a, b = map(int, input().split())
        print(1 if find(a, parent) == find(b, parent) else 0)
    print()