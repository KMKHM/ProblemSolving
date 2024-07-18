"""
가장 가까운 공통 조상
문제: https://www.acmicpc.net/problem/3584
"""
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

t = int(input())

def find_depth(start, graph, depth):
    for v in graph[start]:
        if not depth[v]:
            depth[v] = depth[start] + 1
            find_depth(v, graph, depth)

def find_common_ancestor(u, v):

    while depth[u] != depth[v]:
        if depth[u] > depth[v]:
            u = parent[u]
        else:
            v = parent[v]

    while u != v:
        u, v = parent[u], parent[v]

    return u


for _ in range(t):
    n = int(input())

    graph = [[] for _ in range(n+1)]

    parent = [i for i in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a

    depth = [0] * (n+1)

    root = 0

    for i in range(1, n+1):
        if parent[i] == i:
            root = i
            break

    find_depth(root, graph, depth)

    u, v = map(int, input().split())

    print(find_common_ancestor(u, v))