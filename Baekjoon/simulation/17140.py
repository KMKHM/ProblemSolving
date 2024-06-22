"""
이차원 배열과 연산
문제: https://www.acmicpc.net/problem/17140
"""
import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(3)]

time = 0



def check():
    return board[r-1][c-1] == k

if len(board) >= r and len(board[0]) >= c:
    if check():
        print(time)
        sys.exit(0)

def cal_r():
    max_len = 0
    for i in range(len(board)):
        tmp = []
        dic = sorted(list(Counter(board[i]).items()), key=lambda x: (x[1], x[0]))
        for a, b in dic:
            if a == 0:
                continue
            tmp.append(a)
            tmp.append(b)
        max_len = max(max_len, len(tmp))
        board[i] = tmp

    for i in range(len(board)):
        if len(board[i]) != max_len:
            for _ in range(max_len - len(board[i])):
                board[i].append(0)
    if len(board[0]) > 100:
        for i in range(len(board)):
            board[i] = board[i][:100]

    return board

def cal_c():
    new_board = []
    max_len2 = 0
    for i in range(len(board[0])):
        tmp = [board[j][i] for j in range(len(board))]
        dic = sorted(list(Counter(tmp).items()), key=lambda x: (x[1], x[0]))
        tmp2 = []
        for a, b in dic:
            if a == 0:
                continue
            tmp2.append(a)
            tmp2.append(b)
        max_len2 = max(max_len2, len(tmp2))
        new_board.append(tmp2)

    for i in range(len(new_board)):
        if len(new_board[i]) != max_len2:
            for _ in range(max_len2 - len(new_board[i])):
                new_board[i].append(0)

    if len(new_board[0]) > 100:
        for i in range(len(new_board)):
            new_board[i] = new_board[i][:100]

    q = [[new_board[j][i] for j in range(len(new_board))] for i in range(len(new_board[i]))]

    return q


while 1:
    if time > 100:
        print(-1)
        break

    if len(board) >= len(board[0]):
        board = cal_r()
    else:
        board = cal_c()

    time += 1


    if len(board) >= r and len(board[0]) >= c:
        if check():
            print(time)
            break