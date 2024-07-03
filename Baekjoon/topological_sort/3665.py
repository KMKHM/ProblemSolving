"""
최종 순위
문제: https://www.acmicpc.net/problem/3665
다시 풀기
"""
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))

    indegree = [0] * (n+1)

    graph = [[] for _ in range(n+1)]

    m = int(input())

    if m == 0:
        print(*nums)
        continue

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()

    for num in nums:
        if not indegree[num]:
            q.append(num)

    res = []

    while q:
        cur = q.popleft()
        res.append(cur)

        if not graph[cur]:
            continue

        for v in graph[cur]:
            indegree[v] -= 1
            if not indegree[v]:
                q.append(v)

    print(*res)

