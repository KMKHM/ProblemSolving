"""
이차원 배열과 연산
문제: https://www.acmicpc.net/problem/17140
"""
import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(3)]

# R연산
def r_op(board):
    max_len = 0
    for i in range(len(board)):
        dic = Counter(board[i])
        board[i] = sorted(dic.keys(), key=lambda x: (dic[x], x))
        tmp = []
        for k in board[i]:
            tmp.append(k)
            tmp.append(dic[k])
        board[i] = tmp
        max_len = max(max_len, len(tmp))

    for b in board:
        if len(b) < max_len:
            b += [0] *  (max_len - len(b))
    return board

r_op(board)
for b in board:
    print(b)

# C연산
def c_op():
    pass