"""
https://www.acmicpc.net/problem/19542
"""
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, s, d = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 리프 노드 먼저
leaf = []

parent = [i for i in range(n+1)]

def bfs(start):
    q = deque([start])

    while q:
        cur = q.popleft()
        flag = True
        for v in graph[cur]:
            if parent[cur] != v:
                flag = False
                q.append(v)
                parent[v] = cur
        if flag:
            leaf.append(cur)

bfs(3)


dic = dict()

# 각 리프노드에서 주어진 start 노드로까지의 거리
check = [0] * (n+1)

# def calcuate(leaf_node, cur):
