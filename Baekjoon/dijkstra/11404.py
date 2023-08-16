import sys, heapq

input = sys.stdin.readline

n = int(input())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now_cost, now = heapq.heappop(q)
        if distance[now] < now_cost:
            continue

        for next_cost, next_ in graph[start]:
            cost = now_cost + next_cost
            if distance[next_] > cost:
                distance[next_] = cost
                heapq.heappush(q, (cost, next_))
    return distance[1:]

distance = [sys.maxsize] * (n+1)
print(dijkstra(2, distance))