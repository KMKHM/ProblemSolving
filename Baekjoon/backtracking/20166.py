"""
문자열 지옥에 빠진 호석
문제: https://www.acmicpc.net/problem/20166
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

dic = {}
answer = []

for _ in range(k):
    s = input().rstrip()
    dic[s] = 0
    answer.append(s)

# 8방향
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


def dfs(x, y, start):
    # 만들고자 하는 값과 일치하면 카운트 해주고 리턴
    if start in dic:
        dic[start] += 1

    # 만약 문자열 길이가 5보다 크면 리턴
    if len(start) > 5:
        return

    # 8 방향으로 dfs
    for i in range(8):
        nx, ny = (x + dx[i]) % n, (y + dy[i]) % m
        dfs(nx, ny, start + board[nx][ny])


for r in range(n):
    for c in range(m):
        dfs(r, c, board[r][c])

for s in answer:
    print(dic[s])

