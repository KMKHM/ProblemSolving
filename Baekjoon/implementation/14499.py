"""
주사위 굴리기
문제: https://www.acmicpc.net/problem/14499
"""
import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

# 보드판
board = [list(map(int, input().split())) for _ in range(n)]

# 명령어
command = list(map(int, input().split()))

# 방향
dir = {
    1: [0, 1], # 동
    2: [0, -1], # 서
    3: [-1, 0], # 북
    4: [1, 0]  # 남
}

# 주사위 => 1 2 3 4 5 6 그대로 넣어줌
dice = [0] * 6

def move(d, x, y):
    global dice
    # 동
    if d == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서
    elif d == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북
    elif d == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 남
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0


# 보드판 내에 있는지 검사
def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

# 주사위 굴리기
for c in command:
    dx, dy = dir[c]
    if not check(x + dx, y + dy):
        continue

    x += dx
    y += dy

    move(c, x, y)
    print(dice[0])





