"""
등산코스 정하기
문제: https://school.programmers.co.kr/learn/courses/30/lessons/118669
"""
import heapq
# intensity = 휴식없이 이동해야 하는 시간 중 가장 긴 시간 => 최소로
n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3] # 입구
summits = [5] # 산봉우리

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]

    # 산봉우리 판별
    visited = [0] * (n+1)

    # 산봉우리 표시
    for i in summits:
        visited[i] = 1


    # 그래프 연결
    for a, b, c in paths:
        graph[a].append([c, b])
        graph[b].append([c, a])

    def dijkstra(start, distance):
        q = []
        distance[start] = 0
        heapq.heappush(q, [0, start])

        while q:
            now_cost, now = heapq.heappop(q)
            if distance[now] < now_cost or visited[now]:
                continue

            for next_cost, next_ in graph[now]:

                cost = max(next_cost, now_cost)

                if cost < distance[next_]:
                    distance[next_] = cost
                    heapq.heappush(q, [cost, next_])
        return distance

    print(dijkstra(1, [1e9]*(n+1)))
    return answer


print(solution(n, paths, gates, summits))

