import sys

input = sys.stdin.readline

# 학생 수 , 비교 횟수
n, m = map(int, input().split())

# 그래프
graph = [[0] * (n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1



for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1



for l in graph[1:]:
    print(*l[1:])

