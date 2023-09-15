"""
넴모넴모 (Easy)
문제: https://www.acmicpc.net/problem/14712
"""
n, m = map(int, input().split())

possible = 2 ** (n*m)

impossible = 0

visited = [[0]*m for _ in range(n)]

dx = (1, -1, 0, 0, 1, -1, -1, 1)
dy = (0, 0, -1, 1, 1, -1, 1, -1)

def check(i, j):
    cnt = 0
    for k in range(6):
        ni, nj = i + dx[k], j + dy[k]
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]:
                cnt += 1
                if cnt ==4:
                    return True
    return False



def backtracking(x, y):
    global impossible

    if check(x, y):
        impossible += 1
        return

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                backtracking(nx, ny)
                visited[nx][ny] = 0
    visited[x][y] = 0


backtracking(0, 0)

print(impossible, possible)