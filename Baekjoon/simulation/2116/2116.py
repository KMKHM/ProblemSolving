"""
주사위 쌓기
문제: https://www.acmicpc.net/problem/2116
"""
import sys

input = sys.stdin.readline

"""
1. 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다. 단, 1번 주사위는 마음대로 놓을 수 있다.
2. 이 사각 기둥에는 4개의 긴 옆면이 있다. 이 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다. 
3. 이렇게 하기 위하여 각 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다.
4. 주사위의 개수는 10,000개 이하이며 종류가 같은 주사위도 있을 수 있다.
"""

n = int(input())

dices = [list(map(int, input().split())) for _ in range(n)]

couple = {
    0: 5,
    5: 0,
    2: 4,
    4: 2,
    1: 3,
    3: 1
}

def get_max_sum(bottom, dice):
    for i in range(6):
        if dice[i]==bottom:
            idx = i
            break
    if idx == 0:  # 아랫면 인덱스가 0일 경우
        return (dice[5], max(dice[1], dice[2], dice[3], dice[4]))
    elif idx == 1:
        return (dice[3], max(dice[0], dice[2], dice[4], dice[5]))
    elif idx == 2:
        return (dice[4], max(dice[0], dice[1], dice[3], dice[5]))
    elif idx == 3:
        return (dice[1], max(dice[0], dice[2], dice[4], dice[5]))
    elif idx == 4:
        return (dice[2], max(dice[0], dice[1], dice[3], dice[5]))
    elif idx == 5:
        return (dice[0], max(dice[1], dice[2], dice[3], dice[4]))

ans = 0

for i in range(1, 7):
    tmp_bottom = i
    val = 0
    for j in range(n):
        tmp_bottom, tmp_sum = get_max_sum(tmp_bottom, dices[j])
        val += tmp_sum
    ans = max(ans, val)
print(ans)