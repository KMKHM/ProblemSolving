import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; x2 -= 1; y1 -= 1; y2 -= 1

visited = [[False]*m for _ in range(n)]


dir = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

answer = 0

def bfs(x, y, cnt, direction):

    global answer

    q = deque()
    q.append((x, y, cnt, 0))

    visited[x][y] = True

    while q:
        now_x, now_y, score = q.popleft()
        for i in range(1, 5):
            nx = now_x + dir[i][0]
            ny = now_y + dir[i][1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if nx == x2 and ny == y2:
                    break
                if board[nx][ny] == ".":
                    if now_x != nx or now_y != ny or score == k:
                        visited[nx][ny] = True
                        answer += 1
                        q.append((nx, ny, 0, i))
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny, score+1, i))

bfs(x1, y1, 0)

print(answer)


