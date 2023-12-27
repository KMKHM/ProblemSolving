"""
작업
문제: https://www.acmicpc.net/problem/2056
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

work = [0] * (n+1)

for i in range(n):
    nums = list(map(int, input().split()))
    # 작업시간
    work[i+1] = nums[0]

    if nums[1] == 0:
        continue
    else:
        for v in nums[2:]:
            graph[v].append(i+1)
            indegree[i+1] += 1
dp = [0] * (n+1)

def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = work[i]

    while q:
        now = q.popleft()

        for j in graph[now]:
            indegree[j] -= 1
            dp[j] = max(dp[now] + work[j], dp[j])
            if indegree[j] == 0:
                q.append(j)

topology_sort()

print(max(dp))
