"""
새로운 게임
문제: https://www.acmicpc.net/problem/17780
"""
import sys

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
horse = [0 for _ in range(K)] # 말 리스트

for i in range(K):
    x, y, d = map(int, input().split()) # 말 위치와 방향 입력
    chess[x-1][y-1].append(i)
    horse[i] = [x-1, y-1, d-1]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(chess_num):
    x, y, d = horse[chess_num]
    if chess_num != chess[x][y][0]:
        return 0

    nx = x + dx[d]
    ny = y + dy[d]

    # 파란색이면 반대로 한 칸
    if not 0 <= nx < N or not 0 <= ny < N or color[nx][ny] == 2:
        if 0 <= d <= 1:
            new_d = (d+1) % 2
        else:
            new_d = (d-1) % 2 + 2
        horse[chess_num][2] = new_d
        nx = x + dx[new_d]
        ny = y + dy[new_d]
        # 반대쪽도 파란색 칸이면 이동하지 않음
        if not 0 <= nx < N or not 0 <= ny < N or color[nx][ny] == 2:
            return 0

    chess_set = []
    chess_set.extend(chess[x][y])
    chess[x][y] = []

    # 빨간색인 경우 순서 반대로
    if color[nx][ny] == 1:
        chess_set.reverse()

    for i in chess_set:
        chess[nx][ny].append(i)
        horse[i][:2] = [nx, ny]

    # 말이 4개 이상일 경우 종료
    if len(chess[nx][ny]) >= 4:
        return 1
    return 0

turn = 1
while turn <= 1000:
    for i in range(K):
        flag = move(i)
        if flag:
            print(turn)
            sys.exit()
    turn += 1
print(-1)