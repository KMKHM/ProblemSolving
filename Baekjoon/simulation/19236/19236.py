"""
청소년 상어
문제: https://www.acmicpc.net/problem/19236
"""
import sys
import copy
from collections import deque, Counter

input = sys.stdin.readline

dir = {
    1: [-1, 0],
    2: [-1, -1],
    3: [0, -1],
    4: [1, -1],
    5: [1, 0],
    6: [1, 1],
    7: [0, 1],
    8: [-1, 1]
}

def rotate(d):
    return d % 8 + 1

board = []
dir_board = []
fish = []
fish_loc = Counter()
for i in range(4):
    ls = list(map(int, input().split()))
    tmp_board = []
    tmp_dir_board = []

    for j in range(0, len(ls)-1, 2):
        tmp_board.append(ls[j])
        tmp_dir_board.append(ls[j+1])
        if i == 0 and j == 0:
            continue
        fish.append([ls[j], ls[j+1]])

    board.append(tmp_board)
    dir_board.append(tmp_dir_board)

fish.sort()
fish = deque(fish)

fish_loc = Counter()

for i in range(4):
    for j in range(4):
        fish_loc[board[i][j]] = [i, j]

# 상어의 첫 위치
shark_loc = [0, 0]
shark_dir = dir_board[0][0]
shark_cnt = board[0][0]
# 먹고 시작
board[0][0] = 0
del fish_loc[shark_cnt]

def can_move(r, c):
    if not (0<=r<4 and 0<=c<4):
        return False
    if r == shark_loc[0] and c == shark_loc[1]:
        return False
    return True

def move_fish(fish, board, dir_board, fish_loc):
    new_fish = deque()

    while fish:
        cur_fish, cur_dir = fish.popleft()  # 현재 물고기 번호, 현재 물고기의 방향
        x, y = fish_loc[cur_fish]  # 현재 물고기의 위치
        dx, dy = dir[cur_dir]  # 현재 물고기의 이동 방향

        # 방향 정하기
        while True:
            if not can_move(x + dx, y + dy):  # 이동할 수 없다면
                cur_dir = rotate(cur_dir)  # 45도 회전
                dx, dy = dir[cur_dir]  # 현재 물고기의 이동방향 재정의
            else:
                break
        nx, ny = x + dx, y + dy  # 방향으로 이동
        origin_fish = board[nx][ny]  # 원래 있던 물고기 번호
        board[nx][ny] = cur_fish  # 원래있던 물고기 번호에 현재 물고기 넣고
        board[x][y] = origin_fish  # 현재 물고기 위치에 이동할 방향의 물고기 넣고
        origin_dir = dir_board[nx][ny]
        dir_board[nx][ny] = cur_dir
        dir_board[x][y] = origin_dir
        fish_loc[origin_fish] = [x, y]  # 원래 물고기 위치 변경
        fish_loc[cur_fish] = [nx, ny]  # 현재 물고기 위치 변경
        new_fish.append([cur_fish, cur_dir])
    return new_fish

max_score = 0

def dfs(board, dir_board, fish_loc, fish, shark_loc, shark_dir, score):
    global max_score
    max_score = max(max_score, score)

    # 상태 복사 1번만!
    copied_board = copy.deepcopy(board)
    copied_dir_board = copy.deepcopy(dir_board)
    copied_fish_loc = copy.deepcopy(fish_loc)
    copied_fish = copy.deepcopy(fish)

    # 물고기 이동 (복사본으로만 처리)
    copied_fish = move_fish(copied_fish, copied_board, copied_dir_board, copied_fish_loc, shark_loc)

    # 상어 이동
    x, y = shark_loc
    dx, dy = dir[shark_dir]

    for step in range(1, 4):  # 상어는 최대 3칸까지 이동 가능
        nx, ny = x + dx * step, y + dy * step
        if 0 <= nx < 4 and 0 <= ny < 4 and copied_board[nx][ny] != 0:
            next_fish = copied_board[nx][ny]
            next_dir = copied_dir_board[nx][ny]

            # 다음 상태 복사 (새 재귀 호출용)
            next_board = copy.deepcopy(copied_board)
            next_dir_board = copy.deepcopy(copied_dir_board)
            next_fish_loc = copy.deepcopy(copied_fish_loc)
            next_fish_list = deque([f for f in copied_fish if f[0] != next_fish])

            next_board[x][y] = 0
            next_board[nx][ny] = 0
            del next_fish_loc[next_fish]

            dfs(next_board, next_dir_board, next_fish_loc, next_fish_list, [nx, ny], next_dir, score + next_fish)


dfs(board, dir_board, fish_loc, fish, shark_loc, shark_dir, shark_cnt)

print(max_score)