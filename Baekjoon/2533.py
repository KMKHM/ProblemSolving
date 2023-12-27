"""
사회망 서비스(SNS)
문제: https://www.acmicpc.net/problem/2533
"""
import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n = int(input())

# 그래프
graph = [[] for _ in range(n+1)]

# 그래프 연결
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문체크
check = [0] * (n+1)

# dp 테이블 => dp[i][0] = i가 얼리 어답터인 경우 최소 정점의 수 / dp[i][1] = i가 얼리 어답터가 아닌 경우 최소 정점의 수
dp = [[0, 0] for _ in range(n+1)]

def dfs(v):
    check[v] = 1
    dp[v][0] = 1
    for i in graph[v]:
        if not check[i]:
            dfs(i)
            dp[v][0] += min(dp[i][0], dp[i][1])
            dp[v][1] += dp[i][0]

dfs(1)

print(min(dp[1]))

