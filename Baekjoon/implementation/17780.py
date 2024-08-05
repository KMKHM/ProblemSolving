"""
새로운 게임
문제: https://www.acmicpc.net/problem/17780
"""
import sys
from collections import Counter

input = sys.stdin.readline

n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
check = [list(map(int, input().split())) for _ in range(n)]

# 0 = 횐, 1 = 빨, 2 = 파

dir = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}

# 말의 현재 위치
location = Counter()
direction = Counter()

for i in range(k):
    x, y, d = list(map(int, input().split()))
    check[x][y] = i+1
    location[i+1] = [x, y]
    direction[i+1] = d

# 방향 바꾸는 함수
def change_directino(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    if d == 4: return 3

# 말이 겹치는 부분
plus = [[] for _ in range(k+1)]

turn = 0

def move(num):
    cur_x, cur_y = location[num] # 현재 위치
    nx, ny = cur_x + dir[direction[num]][0], cur_y + dir[direction[num]][1] # 이동한 위치

    if check[nx][ny]: # 이동한 곳에 말이 있는 경우
        plus[check[nx][ny]].append(num) # 말을 올려주고
        check[cur_x][cur_y] = 0 # 이전 위치 초기화

    if board[nx][ny] == 1:
        pass



while turn < 1000:
    for i in range(1, k+1):
        move(i)
    turn += 1
