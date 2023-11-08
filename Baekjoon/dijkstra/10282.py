"""
해킹
문제: https://www.acmicpc.net/problem/10282
"""
import sys, heapq

input = sys.stdin.readline

t = int(input())

def dijkstra(start, distance):
    q = []
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

    cnt, res = 0, 0

    for z in distance:
        if z != sys.maxsize:
            cnt += 1
            res = max(res, z)

    return cnt, res


for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    distance = [sys.maxsize] * (n+1)

    for _ in range(d):
        x, y, r = map(int, input().split())
        graph[y].append((r, x))

    p1, p2 = dijkstra(c, distance)
    print(p1, p2)