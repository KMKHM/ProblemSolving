"""
나의 인생에는 수학과 함께
문제: https://www.acmicpc.net/problem/17265
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [input().split() for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx, dy = (1, 0), (0, 1)

min_val, max_val = int(1e9), -int(1e9)

def calc_val(arr):
    cur = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            if not cur:
                cur.append(int(arr[i]))
            else:
                if cur[-1] == "*":
                    cur[-1] = cur[-2] * int(arr[i])
                elif cur[-1] == "+":
                    cur[-1] = cur[-2] + int(arr[i])
                else:
                    cur[-1] = cur[-2] - int(arr[i])
        else:
            cur.append(arr[i])
    return cur[-1]

def bactracking(x, y, cur_val):
    global min_val, max_val

    if x == n-1 and y == n-1:
        val = calc_val(cur_val)
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = 1
            bactracking(nx, ny, cur_val + [board[nx][ny]])
            visited[nx][ny] = 0

bactracking(0, 0, [board[0][0]])

print(max_val, min_val)