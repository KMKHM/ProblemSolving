import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
# 플레이어, 출구 배열
location = [[0]*n for _ in range(n)]
part = []

for _ in range(m):
    a, b = map(int, input().split())
    part.append([a-1, b-1])
    location[a-1][b-1] += 1

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

ex, ey = map(int, input().split())
ex-=1
ey-=1
location[ex][ey] -= 1

def rotate(arr):
    return list(zip(*arr[::-1]))

def distance(x, y):
    return abs(x - ex) + abs(y - ey)

def pick(x, y):
    f = distance(x, y)
    can = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
            d = distance(nx, ny)
            if d < f:
                can.append([nx, ny])
    return can

def make_rectangle(x, y):
    max_val, min_val = max([x, y, ex, ey]), min([x, y, ex, ey])
    arr = list([0]*(max_val+1) for _ in range(max_val+1))
    for i in range(min_val, max_val+1):
        for j in range(min_val, max_val+1):
            arr[i][j] = board[i][j]
    return [min_val, max_val, arr]

def find_target(location):
    global ex, ey

    new_part = []

    for i in range(n):
        for j in range(n):
            if location[i][j]:
                for _ in range(location[i][j]):
                    new_part.append([i, j])
            if location[i][j] == -1:
                ex, ey = i, j
    return new_part

res = 0

for _ in range(k):
    temp = []
    for a, b in part:
        can = pick(a, b)

        if can:
            if a == ex and b == ey:
                res += 1
                location[a][b] -= 1
            else:
                temp.append(can[0])
        else:
            temp.append([a, b])
    part = temp

    rectangle = []
    for a, b in part:
        rectangle.append(make_rectangle(a, b))
    rectangle.sort(key=lambda x: (len(x[2]), x[0], x[1]))
    m1, m2, rec_result = rectangle[0][0], rectangle[0][1], rectangle[0][2]
    rotate_rect = rotate(rectangle[0][2])

    for i in range(m1, m2+1):
        for j in range(m1, m2+1):
            board[i][j] = rotate_rect[i][j]
            if board[i][j]:
                board[i][j] -= 1

    # location
    temp_location = [[0]*(m2+1) for _ in range(m2+1)]
    for i in range(m1, m2+1):
        for j in range(m1, m2+1):
            temp_location[i][j] = location[i][j]

    temp_location = rotate(temp_location)
    for i in range(m1, m2+1):
        for j in range(m1, m2+1):
            location[i][j] = temp_location[i][j]

    part = find_target(location)

print(res)

for i in board:
    print(*i)