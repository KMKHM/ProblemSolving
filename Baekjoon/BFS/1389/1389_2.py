"""
케빈 베이컨의 6단계 법칙 (플로이드-워셜 사용)
문제: https://www.acmicpc.net/problem/1389
"""
import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

# 플로이드-워셜을 위한 인접 행렬 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_bacon = INF
answer = 0

for i in range(1, n+1):
    bacon = sum(graph[i][1:])
    if bacon < min_bacon:
        min_bacon = bacon
        answer = i

print(answer)