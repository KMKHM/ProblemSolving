n, E, W, N, S = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ls = [(0, 0)]

def dfs(x, y):
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)