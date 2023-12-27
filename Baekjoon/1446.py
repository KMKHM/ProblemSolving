"""
지름길
문제: https://www.acmicpc.net/problem/1446
"""
import sys, heapq

input = sys.stdin.readline

n, d = map(int, input().split())

road = [[] for _ in range(d+1)]

for i in range(d):
    road[i].append((i+1 , 1))

for _ in range(n):
    s, e, r = map(int, input().split())
    if e > d:
        continue
    road[s].append((e, r))

distance = [sys.maxsize] * (d+1)

ans = 0

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now_cost, now = heapq.heappop(q)

        if distance[now] < now_cost:
            continue

        for next_, next_cost in road[now]:
            cost = next_cost + now_cost
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q, (cost, next_))
dijkstra(0)

print(distance[d])



