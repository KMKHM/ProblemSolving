import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N, M, x, Y = map(int, input().split())

graph = [[sys.maxsize] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    _from, _to, weight = map(int, input().split())
    graph[_from][_to] = graph[_to][_from] = weight

    for k in range(N):
        for fromNode in range(N):
            for toNode in range(N):
                graph[fromNode][toNode] = min(graph[fromNode][toNode], graph[fromNode][k] + graph[k][toNode])

day = ans = 0

for i in sorted(graph[Y]):
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