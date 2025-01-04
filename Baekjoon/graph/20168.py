import sys, heapq

input = sys.stdin.readline

# 교차로 수, 골목의 수, 시작 위치, 끝 위치, 가진 돈
n, m, a, b, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append((w, y))
    graph[y].append((w, x))

res = sys.maxsize

distance = [sys.maxsize] * (n+1)
path=[]
def dijkstra(start, end):
    global res
    distance[start] = 0
    q = [[0, start]]
    path.append(start)

    while q:
        cur_cost, cur = heapq.heappop(q)

        # if

        for next_cost, ne in graph[cur]:
            cost = next_cost + cur_cost
            if cost > c:
                continue
            if cost < distance[ne]:
                distance[ne] = cost
                heapq.heappush(q, [cost, ne])
                path.append(ne)
                res=min(res, next_cost)

dijkstra(a, b)
print(distance)
print(res)
print(path)