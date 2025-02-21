"""
진우의 민트초코우유
문제: https://www.acmicpc.net/problem/20208
"""
import sys

input = sys.stdin.readline

# 마을크기, 초기 체력, 늘어나는 체력
n, m, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 집의 위치
start = [0, 0]

# 우유
milk = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            start[0], start[1] = i, j
        if board[i][j] == 2:
            milk.append([i, j])

# 정답
answer = 0


def dfs(x, y, a, cnt):
    global answer

    if abs(x-start[0]) + abs(y-start[1]) <= a:
        answer = max(answer, cnt)

    for r, c in milk:
        if board[r][c] == 2:
            dis = abs(x-r) + abs(y-c)
            if dis <= a:
                board[r][c] = 0
                dfs(r, c, a + h - dis, cnt + 1)
                board[r][c] = 2

dfs(start[0], start[1], m, 0)

print(answer)