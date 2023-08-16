# """
# 줄 세우기
# 문제: https://www.acmicpc.net/problem/2252
# """
#
# import sys
# from collections import deque
#
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# visited = [0] * (n+1)
#
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[b].append(a)
#
# res = deque()
#
# def dfs(x):
#     visited[x] = 1
#     res.append(x)
#
#     for v in graph[x]:
#         if visited[v] == 0:
#             dfs(v)
#
#
#
#
# for i in range(1, n+1):
#     if not graph[i]:
#         res.append(i)
#         visited[i] = 1
#     else:
#         for v in graph[i]:
#             if visited[v] == 1:
#                 continue
#             else:
#
#
#
#
# print(res)