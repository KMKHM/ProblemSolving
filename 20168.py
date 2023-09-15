"""
골목 대장 호석 - 기능성
문제: https://www.acmicpc.net/problem/20168
"""
import sys, heapq

input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())

# 그래프
graph = [[] for _ in range(n+1)]

# 골목
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append([y, k])
    graph[y].append([x, k])


# 최소 비용
tmp = sys.maxsize

# 비용
distance = [sys.maxsize] * (n+1)

# 다익스트라 함수
def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, [start, 0])

    while q:
        now, now_cost = heapq.heappop(q)

        if distance[now] < now_cost:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, [next, cost])

    return distance[end]

print(dijkstra(a, b))
print(distance)
