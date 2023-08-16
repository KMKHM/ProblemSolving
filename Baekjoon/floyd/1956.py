import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[sys.maxsize]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = sys.maxsize

for i in range(1, n+1):
    ans = min(ans, graph[i][i])

print(ans if ans != sys.maxsize else -1)
