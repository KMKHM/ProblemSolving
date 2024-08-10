"""
전단지 돌리기
문제: https://www.acmicpc.net/problem/19542
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, s, d = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = 0

def dfs(start, pre):

    global res

    weight = 0

    for i in graph[start]:
        if i != pre:
            weight = max(weight, dfs(i, start))

    if weight >= d:
        res += 1

    return weight + 1

dfs(s, 0)

print(max(0, 2*(res-1)))