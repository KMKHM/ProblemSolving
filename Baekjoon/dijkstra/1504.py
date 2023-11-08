"""
특정한 최단 경로
문제: https://www.acmicpc.net/problem/1504
"""
import sys, heapq

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    u, v, c = map(int, input().split())
    graph[u].append([c, v])
    graph[v].append([c, u])

a, b = map(int, input().split())

def dijkstra(start, target):
    q = []
    distance = [sys.maxsize] * (n + 1)

    distance[start] = 0

    heapq.heappush(q, [0, start])
    while q:
        now_cost, now = heapq.heappop(q)

        if distance[now] < now_cost:
            continue

        for next_cost, next_ in graph[now]:
            cost = next_cost + now_cost
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q, [cost, next_])

    return distance[target]

first = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, n)
second = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, n)

if first >= sys.maxsize and second >= sys.maxsize:
    print(-1)
else:
    print(min(first, second))