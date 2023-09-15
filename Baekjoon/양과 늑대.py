from copy import deepcopy

answer = - 1
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edge = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

graph = [[] for _ in range(len(info))]
visited = [0]*len(info)

for i, j in edge:
    graph[i].append(j)


def dfs(start, visited, g, w, possible):
    global answer

    if visited[start]:
        return

    visited[start] = 1

    if info[start]:
        w += 1
    else:
        g += 1
        answer = max(answer, g)

    if g <= w:
        return

    possible += graph[start]
    print(start, possible)

    for i in possible:
        dfs(i, deepcopy(visited), g, w, [loc for loc in possible if loc != i and not visited[i]])

dfs(0, visited, 0, 0, [])

print(answer)
