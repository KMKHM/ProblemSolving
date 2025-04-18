"""
종이 조각
문제: https://www.acmicpc.net/problem/14391
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
visted = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

direction = {
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0),
    4: (0, -1)
}

def backtracking(x, y, cur, d):


    print(cur)

    for i in range(1, 5):
        nx, ny = x+direction[i][0], y+direction[i][1]
        if 0<=nx<n and 0<=ny<m:
          if not visted[nx][ny]:
              if not d:
                  visted[nx][ny] = 1
                  backtracking(nx, ny, cur+board[nx][ny], i)
                  visted[nx][ny] = 0
              else:
                  if d == i:
                      visted[nx][ny] = 1
                      backtracking(nx, ny, cur + board[nx][ny], i)
                      visted[nx][ny] = 0


backtracking(0, 0, board[0][0], 0)