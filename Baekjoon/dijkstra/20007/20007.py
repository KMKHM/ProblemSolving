"""
떡 돌리기
문제: https://www.acmicpc.net/problem/20007
"""
import sys, heapq

input = sys.stdin.readline

n, m, x, y = map(int, input().split())

graph = [[] for _ in range(n)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

distance = [sys.maxsize] * n

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        cos, cur = heapq.heappop(q)

        if cos < distance[cur]:
            continue

        for cos_n, nx in graph[cur]:
            cost = cos + cos_n

            if cost < distance[nx]:
                distance[nx] = cost
                heapq.heappush(q, [cost, nx])

dijkstra(y)

print(distance)

day = ans = 0

for i in sorted(distance):
    if i == 0:
        continue

    if i * 2 > x:
        print(-1)
        sys.exit(0)

    if (day + i) * 2 <= x:
        day += i
    else:
        ans += 1
        day = i

print(ans+1)