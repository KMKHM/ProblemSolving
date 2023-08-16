"""
구슬 찾기
문제: https://www.acmicpc.net/problem/2617
"""
import sys

input = sys.stdin.readline

# 구술의 개수, 비교 횟수
n, m = map(int, input().split())

# 정답
answer = 0

# 그래프
bigger_graph, smaller_graph = [[] for _ in range(n+1)], [[] for _ in range(n+1)]

# 진입차수
indegree = [0] * (n+1)

# 진출차수

# 비교 횟수 => a번 노드는 a번 노드 수 보다 작은 노드를 저장한다.
for _ in range(m):
    a, b = map(int, input().split())
    bigger_graph[a].append(b)
    smaller_graph[b].append(a)

# dfs
def dfs(graph, start):
    global cnt
    for v in graph[start]:
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            dfs(graph, v)

# 가운데
mid = (n+1) // 2


for i in range(1, n+1):
    visited = [0] * (n + 1)

    cnt = 0
    dfs(bigger_graph, i)
    if cnt >= mid:
        answer += 1

    cnt = 0
    dfs(smaller_graph, i)
    if cnt >= mid:
        answer += 1






print(answer)

