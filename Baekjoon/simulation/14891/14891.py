"""
톱니바퀴
문제: https://www.acmicpc.net/problem/14891
"""
import sys
from collections import deque

input = sys.stdin.readline

wheels = []

for _ in range(4):
    wheels.append(deque(map(int, list(input().rstrip()))))

# 회전 횟수
k = int(input())

# 회전
op = [list(map(int, input().split())) for _ in range(k)]

# 회전함수
def rotate_wheel(wheel, direction):
    if direction != 0:
        wheel.rotate(direction)

score = 0

def decide_rotate(num, d):
    arr = [0] * 4
    arr[num] = d  # 현재 톱니바퀴의 회전 방향 설정

    # 오른쪽 방향으로 전파
    for i in range(num, 3):
        if wheels[i][2] != wheels[i + 1][6]:  # 맞닿은 극이 다르면 반대 방향 회전
            arr[i + 1] = -arr[i]
        else:
            break

    # 왼쪽 방향으로 전파
    for i in range(num, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:  # 맞닿은 극이 다르면 반대 방향 회전
            arr[i - 1] = -arr[i]
        else:
            break

    return arr


for num, r in op:
    target = num - 1

    arr = decide_rotate(target, r)

    for i in range(4):
        rotate_wheel(wheels[i], arr[i])

score += 1 if wheels[0][0] == 1 else 0
score += 2 if wheels[1][0] == 1 else 0
score += 4 if wheels[2][0] == 1 else 0
score += 8 if wheels[3][0] == 1 else 0

print(score)