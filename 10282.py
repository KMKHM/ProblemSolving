import sys, heapq


input = sys.stdin.readline

INF = sys.maxsize

t = int(input())


for _ in range(t):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    dist = [INF] * (n+1)

    for _ in range(d):
        a, b, t = map(int, input().split())
        graph[b].append([a, t])

    def dijkstra(x,cnt):
        cnt += 1
        dist[x] = 0
        q = []
        heapq.heappush(q, [0, x])
        while q:
            cur_cost, now = heapq.heappop(q)

            if dist[now] < cur_cost:
                continue

            for next, cost in graph[now]:
                virus = cur_cost + cost
                if virus < dist[next]:
                    dist[next] = virus
                    heapq.heappush(q, [virus, next])
                    cnt += 1
        return cnt

    print(dijkstra(c, 0))


