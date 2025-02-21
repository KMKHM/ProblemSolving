"""
배열 돌리기 4
문제: https://www.acmicpc.net/problem/17406
"""
import sys
from copy import deepcopy
from itertools import permutations

input = sys.stdin.readline

n, m, k = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]

op = [list(map(int, input().split())) for _ in range(k)]

# 정답
ans = sys.maxsize

# 회전 방향 => 오른쪽, 아래, 왼쪽, 위쪽
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

def rotate(r, c, s, arr):
    # 사각형 시작 부분
    r1, c1 = r-s-1, c-s-1
    # 사각형 끝 부분
    r2, c2 = r+s-1, c+s-1

    # 종료조건
    end_condtion = ((r1+r2) //2, (c1+c2)//2)

    # 현재값
    now = 0

    # 현재방향
    dir = 0

    while True:
        # 시작 위치
        x, y = r1, c1
        while True:
            nx, ny = x + dx[dir], y + dy[dir]

            if x == r1 + 1 and y == c1:
                arr[r1][c1] = arr[r1+1][c1]
                arr[x][y] = now
                dir = 0
                break

            # 방향 바꾸기
            if nx < r1 or nx > r2 or ny < c1 or ny > c2:
                dir += 1
                continue

            arr[x][y], now = now, arr[x][y]

            x, y = nx, ny
        r1, c1 = r1 + 1, c1 + 1
        r2, c2 = r2 - 1, c2 - 1

        if (r1, c1) == end_condtion:
            break


for case in permutations(op):
    arr = deepcopy(nums)

    for r, c, s in case:
        rotate(r, c, s, arr)

    for val in arr:
        ans = min(ans, sum(val))

print(ans)