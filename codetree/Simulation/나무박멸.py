import sys
input = sys.stdin.readline

n, m, k, c = map(int, input().split())
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
kx, ky = (1, 1, -1, -1), (1, -1, 1, -1)

board = [list(map(int, input().split())) for _ in range(n)]
erase = [[0]*n for _ in range(n)]  # 제초 잔여 수명
res = 0

def check(x, y): 
    return 0<=x<n and 0<=y<n

def decay_herbicide():
    for i in range(n):
        for j in range(n):
            if erase[i][j] > 0:
                erase[i][j] -= 1

def grow():
    # 나무가 있는 칸만 성장
    inc = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if check(nx, ny) and board[nx][ny] > 0:
                        cnt += 1
                inc[x][y] = cnt
    for x in range(n):
        for y in range(n):
            if inc[x][y]:
                board[x][y] += inc[x][y]

def breed():
    add = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] > 0:
                empties = []
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if check(nx, ny) and board[nx][ny] == 0 and erase[nx][ny] == 0:
                        empties.append((nx, ny))
                if empties:
                    val = board[x][y] // len(empties)
                    if val > 0:
                        for a, b in empties:
                            add[a][b] += val
    for i in range(n):
        for j in range(n):
            if add[i][j]:
                board[i][j] += add[i][j]

def kill_count_at(x, y):

    if board[x][y] <= 0:
        base = 0
    else:
        base = board[x][y]
    total = base

    for d in range(4):
        for step in range(1, k+1):
            nx, ny = x + kx[d]*step, y + ky[d]*step
            if not check(nx, ny): break
            if board[nx][ny] == -1:  # 벽이면 즉시 중단
                break
            if board[nx][ny] == 0:   # 빈칸이면 그 칸까지 제초는 닿지만 더는 진행 안 함
                total += 0
                break
            # 나무가 있으면 누적
            total += board[nx][ny]
    return total

def choose_cell():
    best = -1
    cx, cy = 0, 0
    for x in range(n):
        for y in range(n):
            val = kill_count_at(x, y)
            if val > best:
                best = val
                cx, cy = x, y
            elif val == best:
                if (x, y) < (cx, cy):
                    cx, cy = x, y
    return cx, cy, max(0, best)

def spread(x, y):
    killed = 0

    if board[x][y] > 0:
        killed += board[x][y]
        board[x][y] = 0
    erase[x][y] = c

    for d in range(4):
        for step in range(1, k+1):
            nx, ny = x + kx[d]*step, y + ky[d]*step
            if not check(nx, ny):
                break
            erase[nx][ny] = c
            if board[nx][ny] in [-1, 0]:
                break

            killed += board[nx][ny]
            board[nx][ny] = 0
    return killed

for _ in range(m):
    decay_herbicide()
    grow()
    breed()
    x, y, _ = choose_cell()
    res += spread(x, y)

print(res)