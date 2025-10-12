"""
https://www.acmicpc.net/problem/1939
"""
import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

s, e = map(int, input().split())

distance = [0] * (n+1)

def dijkstra(start):
    q = []
    distance[start] = sys.maxsize
    heapq.heappush(q, [-sys.maxsize, start])

    while q:
        now_cost, now = heapq.heappop(q)
        now_cost = -now_cost

        if distance[now] > now_cost:
            continue

        for next_cost, next in graph[now]:
            cost = min(now_cost, next_cost)
            if distance[next] < cost:
                distance[next] = cost
                heapq.heappush(q, [-cost, next])

dijkstra(s)

print(distance[e])