"""
사탕 게임
문제: https://www.acmicpc.net/problem/3085
"""
import sys

input = sys.stdin.readline

n = int(input())

candy = [list(input().rstrip()) for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)

ans = 0

def check():
    cnt = 0
    # 같은 행
    for i in range(n):
        temp = candy[i]
        temp_cnt = 0
        for j in range(n-1):
            c = temp[j]
            if c == temp[j+1]:
                temp_cnt += 1



for i in range(n):
    for j in range(n):
        tmp = candy[i][j]
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if tmp != candy[nx][ny]:
                    candy[i][j] = candy[nx][ny]
                    candy[nx][ny] = tmp

