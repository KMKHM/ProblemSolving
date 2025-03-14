"""
마법사 상어와 파이어볼
문제: https://www.acmicpc.net/problem/20056
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]

operation = []

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    operation.append([r-1, c-1, m, s, d])

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

for _ in range(k):

    while operation:
        cur_r, cur_c, cur_m, cur_s, cur_d = operation.pop()
        next_r = (cur_r + dx[cur_d] * cur_s) % n
        next_c = (cur_c + dy[cur_d] * cur_s) % n
        board[next_r][next_c].append([cur_m, cur_s, cur_d])

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                cnt = len(board[i][j])
                val_m, val_s, val_d = 0, 0, 0
                even, odd = 0, 0

                while board[i][j]:
                    pm, ps, pd = board[i][j].pop()
                    val_m += pm
                    val_s += ps
                    even += 1 if pd % 2 == 0 else 0
                    odd += 1 if pd % 2 == 1 else 0

                val_m //= 5
                val_s //= cnt
                val_d = [0, 2, 4, 6] if cnt == even or cnt == odd else [1, 3, 5, 7]

                if val_m == 0:
                    continue
                else:
                    for dir in val_d:
                        operation.append([i, j, val_m, val_s, dir])

            elif len(board[i][j]) == 1:
                operation.append([i, j] + board[i][j].pop())

print(sum(i[2] for i in operation))