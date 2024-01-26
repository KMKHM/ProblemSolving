import sys
N, M = map(int, input().split())
relations = [[] for _ in range(N)]

# 양방향 그래프
for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

visited = [False] * N

def dfs(idx, depth):
    if depth == 4:
        print(1)
        sys.exit(0)

    for i in relations[idx]:
        if not visited[i]:
            visited[idx] = True
            dfs(i, depth + 1)
            visited[idx] = False


for i in range(N):
    visited[i] = True
    dfs(i, 0)


print(0)
