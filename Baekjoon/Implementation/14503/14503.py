"""
로봇 청소기
문제: https://www.acmicpc.net/problem/14503
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

direction = {
    0: [-1, 0], # 북
    1: [0, 1], # 동
    2: [1, 0], # 남
    3: [0, -1] # 서
}

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

visited = [[0 for _ in range(m)] for _ in range(n)]

# 청소된 칸이 있다면 False
def is_check(r, c):
    for i in range(4):
        x, y = r + dx[i], c + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if not visited[x][y] and board[x][y] == 0: # 청소하지 않은 빈 칸인 경우
                return True
    return False

cur_direction = direction[d]

# 후진 방향
def get_back_directoin(cur_direction):
    x, y = cur_direction
    return [-x, -y]

# 반시계 방향 90도 회전
def rotate(d):
    if d == 0:
        return 3
    return d - 1

# 후진 방향으로 갈 수 있는지
def can_back(x, y, cur_direction):
    x += cur_direction[0]
    y += cur_direction[1]
    if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
        return True
    return False

def can_move(x, y, cur_direction):
    x += cur_direction[0]
    y += cur_direction[1]
    if 0 <= x < n and 0 <= y < m and board[x][y] == 0 and not visited[x][y]: # 빈 칸이고 청소되지 않은 칸인 경우
        return True
    return False

# 청소한 칸의 수
res = 0


while True:
    # 청소되지 않은 경우 청소
    if not visited[r][c]:
        visited[r][c] = 1
        res += 1

    # 주변에 모두  청소된 칸인 경우
    if not is_check(r, c):
        temp_dir_x = -cur_direction[0]
        temp_dir_y = -cur_direction[1]
        if can_back(r, c, [temp_dir_x, temp_dir_y]): # 후진할 수 있으면
            r, c = r + temp_dir_x, c + temp_dir_y # 후진한다.
        else: # 후진할 수 없다면
            break
    else: # 청소되지 않는 칸이 있을 경우
        # 반 시계 방향 회전
        d = rotate(d)
        cur_direction = direction[d]
        if can_move(r, c, cur_direction):
            r, c = r + cur_direction[0], c + cur_direction[1]
        continue

print(res)
