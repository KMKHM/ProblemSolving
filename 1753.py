import sys, heapq

input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

dist = [INF] * (n+1)

v = int(input())

for _ in range(m):
    a, b, cost = map(int, input().split())
    # if b in graph[a]:
    #     for vertex in graph:
    #         if vertex[0] == b:
    #             vertex[1] = min(vertex[1], cost)
    # else:
    graph[a].append([b, cost])

def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        for elem in graph[cur]:
            c = cur_dist + elem[1]
            if c < dist[elem[0]]:
                dist[elem[0]] = c
                heapq.heappush(q, [c, elem[0]])

dijkstra(v)


for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)