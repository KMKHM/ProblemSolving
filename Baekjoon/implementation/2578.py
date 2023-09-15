"""
빙고
문제: https://www.acmicpc.net/problem/2578
"""
import sys

input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]

def check():
    cnt = 0

    # 가로 빙고
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt += 1

    # 세로 빙고
    for i in range(5):
        tmp = 0
        for j in range(5):
            if bingo[j][i] > 0:
                tmp = 1
                break
        if tmp == 0:
            cnt += 1
    # 대각선1
    tmp2 = 0
    for i in range(5):
        if bingo[i][i] > 0:
            tmp2 = 1
            break
    if tmp2 == 0:
        cnt += 1

    # 대각선2
    tmp3 = 0
    for i in range(5):
        if bingo[i][4-i] > 0:
            tmp3 += 1
            break
    if tmp3 == 0:
        cnt += 1

    return cnt

def find(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                return

ans = 0
flag = 0
while 1:
    nums = list(map(int, input().split()))

    for num in nums:
        find(num)
        flag += 1
        ans += 1
        if flag >= 12:
            if check() >= 3:
                print(ans)
                sys.exit(0)