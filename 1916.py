"""
최소비용 구하기
"""
import sys, heapq

input = sys.stdin.readline

INF = sys.maxsize

# 도시의 개수
n = int(input())

# 버스의 수
m = int(input())

# 그래프
graph = [[] for _ in range(n+1)]

# 그래프 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

# 거리 테이블
dist = [INF] * (n+1)

def dijkstra(start):
    dist[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while q:
        cur_dist, now = heapq.heappop(q)

        if dist[now] < cur_dist:
            continue

        for i in graph[now]:
            cur_cost = cur_dist + i[1]
            if cur_cost < dist[i[0]]:
                dist[i[0]] = cur_cost
                heapq.heappush(q, [cur_cost, i[0]])

s, e = map(int, input().split())

dijkstra(s)
print(dist[e])
