"""
회전 미로 탐색
문제: https://www.acmicpc.net/problem/22949
"""
import sys, copy
from collections import deque

input = sys.stdin.readline

k = int(input())

# 원본 배열
original = [list(input().rstrip()) for _ in range(4*k)]


# 이동방향 => 상하좌우, 가만히 있기
dx, dy = (1, -1, 0, 0, 0), (0, 0, 1, -1, 0)

# 배열 회전
def rotate(arr):
    tuples = zip(*arr[::-1])
    return [list(e) for e in tuples]

# 시작 지점, 목표 지점
sx, sy, ex, ey = 0, 0, 0, 0

for i in range(4*k):
    for j in range(4*k):
        if original[i][j] == "S":
            sx, sy = i, j
        if original[i][j] == "E":
            ex, ey = i, j

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])

    while q:
        now_x, now_y, t = q.popleft()
        for i in range(5):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < 4*k and 0 <= ny < 4*k:
                q.append([nx, ny, t+1])

# 어느 영역에 있는지 판단
def check(x, y):
    if 0 <= x < 4*k//2 and 0 <= y < 4*k//2:
        return 1
    elif 0 <= x < 4*k//2 and 4*k//2 <= y < 4*k:
        return 2
    elif 4*k//2 <= x < 4*k and 0 <= y < 4*k//2:
        return 3
    else:
        return 4

# 부분배열돌리기
def rotate_part(o):
    repli = copy.deepcopy(original)

    if o == 1:
        arr1 = rotate([r[:4*k//2] for r in original[:4*k//2]])
        for i in range(4*k//2):
            for j in range(4*k//2):
                repli[i][j] = arr1[i][j]
        return repli
    elif o == 2:
        arr2 = rotate([r[4*k//2:] for r in original[:4*k//2]])
        for i in range(4*k//2, 4*k):
            for j in range(4*k//2):
                repli[i][j] = arr2[i-4*k//2][j]
        return repli
    elif o == 3:
        arr3 = rotate([r[:4 * k // 2] for r in original[4 * k // 2:]])
        for i in range(4*k//2):
            for j in range(4*k//2, 4 * k):
                repli[i][j] = arr3[i][j-4*k//2]
        return repli
    elif o == 4:
        arr4 = rotate([r[4 * k // 2:] for r in original[4 * k // 2:]])
        for i in range(4*k//2), 4 * k:
            for j in range(4*k//2, 4 * k):
                repli[i][j] = arr4[i-4*k//2][j-4*k//2]
        return repli

print(rotate_part(2))