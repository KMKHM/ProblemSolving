"""
민준이와 마산 그리고 건우
문제: https://www.acmicpc.net/problem/18223
"""
import sys, heapq

input = sys.stdin.readline

v, e, p = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start, target, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_cost, now = heapq.heappop(q)
        if now_cost < distance[now]:
            continue

        for next_cost, next_ in graph[now]:
            cost = next_cost + now_cost
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q, (cost, next_))
    return distance[target]


min_val = dijkstra(1, v, [sys.maxsize] * (v+1))

answer = dijkstra(1, p, [sys.maxsize] * (v+1)) + dijkstra(p, v, [sys.maxsize] * (v+1))

if answer == min_val:
    print("SAVE HIM")
else:
    print("GOOD BYE")