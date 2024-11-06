"""
최소비용 구하기 2
문제: https://www.acmicpc.net/problem/11779
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [sys.maxsize] * (n+1)
move = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        cur_cost, cur = heapq.heappop(q)

        if cur_cost > distance[cur]:
            continue

        for nx, nx_cost in graph[cur]:
            cost = cur_cost + nx_cost
            if cost < distance[nx]:
                distance[nx] = cost
                move[nx] = cur
                heapq.heappush(q, [cost, nx])

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
path = [end]
now = end

while now != start:
    now = move[now]
    path.append(now)
print(len(path))
print(*path[::-1])