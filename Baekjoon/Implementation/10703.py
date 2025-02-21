"""
유성
문제: https://www.acmicpc.net/problem/10703
"""
import sys

input = sys.stdin.readline

r, s = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

ans = [["."] * s for _ in range(r)]

# 이동할 수 있는 거리
distance = sys.maxsize


for i in range(s):
    sky, ground = -sys.maxsize, sys.maxsize
    for j in range(r):
        if board[j][i] == "X":
            sky = max(sky, j)
        if board[j][i] == "#":
            ground = min(ground, j)
    distance = min(distance, abs(ground-sky)-1)

for i in range(r):
    for j in range(s):
        if board[i][j] == "X":
            ans[i+distance][j] = "X"
        if board[i][j] == "#":
            ans[i][j] = "#"

for i in range(r):    # 결과 출력
    for j in range(s):
        sys.stdout.write(ans[i][j])
    sys.stdout.write('\n')
