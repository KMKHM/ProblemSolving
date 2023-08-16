"""
트리
문제: https://www.acmicpc.net/problem/1068
"""
import sys

input = sys.stdin.readline

n = int(input())

# 그래프
graph = [[] for i in range(n)]

nums = list(map(int, input().split()))

# 지울 노드
v = int(input())

outdegree = [0] * n

# 루트 노드
root = 0

# 방문
visited = [0] * n

# 그래프 연결
for i in range(n):
    if nums[i] == -1:
        root = i
        continue

    outdegree[nums[i]] += 1
    graph[nums[i]].append(i)

def dfs(r):
    if r == v:
        print(0)
        sys.exit(0)

    visited[r] = 1
    for node in graph[r]:
        if not visited[node]:
            if node == v:
                outdegree[r] -= 1
                continue
            visited[node] = 1
            dfs(node)
dfs(root)

for i in range(n):
    if visited[i] == 0:
        outdegree[i] = -1
        for j in graph[i]:
            outdegree[j] = -1

print(outdegree.count(0))
