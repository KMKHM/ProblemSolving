"""
아기 상어
문제: https://www.acmicpc.net/problem/16236
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 보드판
nums = list(map(int, input().split()))

# 상어 처음 크기 = 2
size = 2

# 1초에 상하좌우
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

# 자신 보다 큰 물고기 있는 칸 못지나감
def check(x1, y1, x2, y2):
    if nums[x1][y1] < nums[x2][y2]:
        return False
    return True

# 물고기 X => 엄마한테 도움
# 1마리면 먹으러감
# 1마리보다 많으면 가장 가까운 거리에있는 물고기
# 칸의 최소값 => 위 => 왼쪽
# 이동시간 1초
# 먹으면 빈 칸
# 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가

# def check_fish():
#     return sum(sum(i) for i in nums) == 0

def check_fish():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if nums[i][j] == size:
                cnt += 1
    return size == cnt


# 물고기 초기 위치
x, y = 0, 0

for i in range(n):
    for j in range(n):
        if nums[i][j] == 9:
            x, y = i, j
            break

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    eat = []

    while q:
        curx, cury = q.popleft()
        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if nums[x][y] > nums[nx][ny] and nums[nx][ny] != 0:
                    visited[nx][ny] = visited[curx][cury] + 1
                    q.append(1)




while True:
    if not check_fish():
        break

