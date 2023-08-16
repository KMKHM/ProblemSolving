"""
떡 돌리기
문제: https://www.acmicpc.net/problem/20007
"""
import sys, heapq

input = sys.stdin.readline

# x = 최대 거리, y = 집
n, m, x, y = map(int, input().split())

# 그래프
graph = [[] for _ in range(n)]

# 간선
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

# 거리
dist = [sys.maxsize] * n

def dijkstra(start):
    q = [[0, start]]
    dist[start] = 0

    while q:
        now_cost, now = heapq.heappop(q)

        if dist[now] < now_cost:
            continue

        for next_cost, next_ in graph[now]:
            cost = next_cost + now_cost
            if cost < dist[next_]:
                dist[next_] = cost
                heapq.heappush(q, [cost, next_])

dijkstra(y)

for k in dist:
    if k == y:
        continue
    if k*2 > x:
        print(-1)
        sys.exit(0)

tmp = sum(dist) * 2

answer = 1
cur = 0
for k in dist:
    if cur + 2*k <= x:
        cur += 2*k
    else:
        answer += 1
        cur = 2*k


