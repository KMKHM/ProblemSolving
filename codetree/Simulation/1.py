"""
싸움땅
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

check = [[[] for _ in range(n)] for _ in range(n)]

point = [0] * (m+1)
player = defaultdict(list)

for i in range(m):
    # 초기 위치, 방향, 초기 능력치
    x, y, d, s = map(int, input().split())
    check[x-1][y-1].append(i + 1)
    player[i+1] = [x-1, y-1, d, s, 0]

direction = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

# 가다가 벽만남
def reverse(d):
    if d == 0:
        return 2
    if d == 2:
        return 0
    if d == 1:
        return 3
    return 1

# 지고 가다가 벽만남 90도 회전
def rotate(d):
    return 0 if d == 3 else d + 1


# 0 빈칸, 나머지는 총
# 이기면 능력치 + 총 능력치의 합의 차이 만큼 포인트 획득
"""
지면 총 내려놓고 원래 방향으로 한 칸이동
이동하려는 칸에 다른 플레이어 있거나 격자 밖이면 오른쪽으로 90도회전
"""

# 이동
def move(x, y, d, player_num):
    fail = False
    while True:
        nx, ny = x + direction[d][0], y + direction[d][1]
        # 안지고 벽만나는 경우
        if not (0 <= nx < n and 0 <= ny < n):
            d = reverse(d)
            continue

        # 총 만나는 경우 줍고 플레이어 이동
        if not check[nx][ny]:
            player_gun = player[player_num][-1]
            player[player_num][-1] = max(board[nx][ny], player_gun); board[nx][ny] = min(board[nx][ny], player_gun)
            check[x][y].remove(player_num); check[nx][ny].append(player_num)
            player[player_num][0], player[player_num][1] = nx, ny
            return

        # 이미 플레이어가 있는 곳으로 이동한 경우
        elif check[nx][ny]:
            # 원래 플레이어
            origin_player_num = check[nx][ny][0]
            # 이동하는 플레이어
            cur_player_num = player_num
            # 원래있던 플레이어의 공격력
            origin_player_attack = player[check[nx][ny][0]][-1] + player[check[nx][ny][0]][-2]
            # 현재 플레이어의 공격력
            cur_player_attack = player[check[x][y][0]][-1] + player[check[x][y][0]][-2]
            # 원래 능력치
            origin_ability, cur_ability = player[origin_player_num][-2], player[cur_player_num][-2]

            if origin_player_attack < cur_player_attack:
                point[cur_player_num] += (cur_player_attack - cur_ability)
                check[x][y].remove(player_num)
                check[nx][ny].append(player_num)
                return
            elif origin_player_attack > cur_player_attack:
                point[origin_player_num] += (origin_player_attack - origin_ability)
                fail = True
            else: # 같은 경우
                if origin_ability > cur_ability:
                    point[origin_player_num] += (origin_player_attack - origin_ability)
                    fail = True
                else:
                    point[cur_player_num] += (cur_player_attack - cur_ability)
                    check[x][y].remove(player_num)
                    check[nx][ny].append(player_num)
                    return

            if fail:# 진 경우
                while True:
                    nnx, nny = nx + direction[d][0], ny + direction[d][1]
                    if not (0 <= nnx < n and 0 <= nny < n) or check[nnx][nny]:
                        d = rotate(d)
                        continue
                    player_gun = player[player_num][-1]
                    player[player_num][-1] = max(board[nnx][nny], player_gun)
                    board[nnx][nny] = min(board[nnx][nny], player_gun)
                    check[x][y].remove(player_num)
                    check[nnx][nny].append(player_num)
                    player[player_num][0], player[player_num][1] = nnx, nny
                    break
                return


for _ in range(k):
    for i in range(1, m+1):
        x, y, d, s, g = player[i]
        move(x, y, d, i)
        # print(point[i])

print(point)

for i in check:
    print(*i)