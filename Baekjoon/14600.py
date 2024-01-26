"""
샤워실 바닥 깔기 (Small)
문제: https://www.acmicpc.net/problem/14600
"""
import sys

input = sys.stdin.readline
print(86400000*7)
k = int(input())

# 한 변의 길이
square = 2 ** k


# 배수구 위치 => 가장 왼쪽 아래 = (1,1) / 가장 오른쪽 위 = (2**k, 2**k) => 일단 좌표대로 채운다음 거꾸로 출력하면된다.
x, y = map(int, input().split())

# 3칸을 차지하는 ㄱ자 모양 타일 사용

# 타일
board = [[0] * (square+1) for _ in range(square+1)]

# 배수구 표시
board[y][x] = -1


num = 0

def prin1():
    for i in range(square, 0, -1):
        for j in range(1, square+1):
            print(board[i][j], end=" ")
        print()
    print("----")

def prin1():
    for i in range(1, square+1):
        for j in range(1, square+1):
            print(board[i][j], end=" ")
        print()
    print("----")

def check(r, c, length):
    for i in range(r, r+length):
        for j in range(c, c+length):
            if board[i][j] != 0:
                return False
    return True
def recur(r, c, size):
    global num
    num += 1

    # size = 4 => tmp = 2
    tmp = size // 2

    # 1
    if check(r, c, tmp):
        board[r+tmp-1][c+tmp-1] = num
        prin1()
    # 2
    if check(r+tmp, c, tmp):
        board[r+tmp][c+tmp-1] = num

    # 3
    if check(r, c+tmp, tmp):
        board[r+tmp-1][c+tmp] = num

    # 4
    if check(r+tmp, c+tmp, tmp):
        board[r+tmp][c+tmp] = num

    if size == 2:
        return

    recur(r, c, tmp)
    recur(r+tmp, c, tmp)
    recur(r, c+tmp, tmp)
    recur(r+tmp, c+tmp, tmp)

recur(1, 1, square)






