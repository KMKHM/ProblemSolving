"""
연구소
문제: https://www.acmicpc.net/problem/14502
"""
import sys, copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

blank = []
virus = []
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)


for i in range(n):
    ls = list(map(int, input().split()))
    board.append(ls)
    for j in range(m):
        if ls[j] == 0:
            blank.append([i, j])
        if ls[j] == 2:
            virus.append([i, j])

candidate = []
def get_candidate(level, start, arr):
    if level == 3:
        candidate.append(arr[:])
        return

    for i in range(start, len(blank)):
        get_candidate(level + 1, i + 1, arr + [blank[i]])

get_candidate(0, 0, [])

def bfs(q):
    temp = copy.deepcopy(board)
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and  temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append([nx, ny])
    cnt = 0
    for i in range(n):
        cnt += temp[i].count(0)
    return cnt

ans = 0

for e in candidate:
    for r, c in e:
        board[r][c] = 1
    q = deque(virus)
    ans = max(ans, bfs(q))
    for r, c in e:
        board[r][c] = 0

print(ans)