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


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

distance = [sys.maxsize] * n

# 다익스트라
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

tmp = sorted([distance[i] for i in range(len(distance)) if i != y])

day = 0

ans = 0

for i in range(len(tmp)):
    if tmp[i] * 2 > x:
        print(-1)
        sys.exit(0)

    if (day + tmp[i]) * 2 <= x:
        day += tmp[i]
    else:
        ans += 1
        day = tmp[i]

print(ans+1)
