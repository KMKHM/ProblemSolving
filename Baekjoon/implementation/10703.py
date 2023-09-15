"""
유성
문제: https://www.acmicpc.net/problem/10703
"""
import sys, copy

input = sys.stdin.readline

r, s = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]



mete = []

for i in range(r):
    for j in range(s):
        if board[i][j] == "X":
            mete.append([i, j])


x, y = mete[-1][0], mete[-1][1]

cnt = 0
while 1:
    if board[x+1][y] != "#":
        x += 1
        cnt += 1
    else:
        break

tmp = copy.deepcopy(mete)

for i in range(len(mete)):
    mete[i][0] += cnt
    board[mete[i][0]][mete[i][1]] = "X"

    if tmp[i] not in mete:
        board[tmp[i][0]][tmp[i][1]] = "."


for i in range(r):    # 결과 출력
    for j in range(s):
        sys.stdout.write(board[i][j])
    sys.stdout.write('\n')
