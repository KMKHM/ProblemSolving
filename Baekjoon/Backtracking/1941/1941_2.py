"""
소문난 칠공주
문제: https://www.acmicpc.net/problem/1941
"""
import sys

from itertools import combinations
from collections import deque

input = sys.stdin.readline

board = [input().strip() for _ in range(5)]

positions = [(i, j) for i in range(5) for j in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 인접 확인용 BFS&DFS 함수
def is_adjacent(selected):
    queue = deque([selected[0]])
    visited = set([selected[0]])
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) in selected and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                count += 1

    # 7개 모두 연결되어 있는지 확인
    return count == 7

# 경우의 수 계산
count = 0
for comb in combinations(positions, 7):
    # S가 4명 이상인지 확인
    s_count = sum(1 for x, y in comb if board[x][y] == 'S')
    if s_count < 4:
        continue

    # 인접한지 확인
    if is_adjacent(comb):
        count += 1

print(count)
