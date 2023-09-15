"""
점프왕 쩰리 (Large)
문제: https://www.acmicpc.net/problem/16174
"""
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx, dy = (0, 1), (1, 0)

def dfs(x, y):

    visited[x][y] = 1


    if (x, y) == (n-1, n-1):
        print("HaruHaru")
        sys.exit(0)
        return

    for i in range(2):
        nx = x + dx[i] * board[x][y]
        ny = y + dy[i] * board[x][y]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                dfs(nx, ny)


dfs(0, 0)

print("Hing")