"""
크로스워드 퍼즐 쳐다보기
문제: https://www.acmicpc.net/problem/3005
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

res = []

board = []

for _ in range(n):
    s = input().rstrip()
    if "#" not in s:
        res.append(s)
    else:
        for c in s.split("#"):
            if len(c) >= 2:
                res.append(c)
    board.append(list(s))

for j in range(m):
    tmp = ""
    for i in range(n):
        if board[i][j] != "#":
            tmp += board[i][j]
        else:
            if len(tmp) >= 2:
                res.append(tmp)
            tmp = ""
    if len(tmp) >= 2:
        res.append(tmp)


print(sorted(res)[0])
