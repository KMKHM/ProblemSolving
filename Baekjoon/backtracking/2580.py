"""
스도쿠
문제: https://www.acmicpc.net/problem/2580
"""
"""
0 3 5 4 6 9  2 7 8
7 8 2 1 0 5  6 0 9
0 6 0 2 7 8  1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""
import sys

# 수도쿠 판
sudokku = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸의 좌표
zero = [(x, y) for x in range(9) for y in range(9) if sudokku[x][y] == 0]

# 빈 칸의 수
n = len(zero)

# 행 검사
def check_row(a, num):
    if num in sudokku[a]:
        return False
    return True

# 열 검사
def check_col(b, num):
    for i in range(9):
        if sudokku[i][b] == num:
            return False
    return True

# 부분 검사
def check_part(a, b, num):
    a, b = a//3 * 3, b//3 *3
    for i in range(3):
        for j in range(3):
            if sudokku[a+i][b+j] == num:
                return False
    return True

def bt(level):
    # 모두 채운 경우
    if level == n:
        for i in range(9):
            print(*sudokku[i])
        sys.exit(0)

    for num in range(1, 10):
        x, y = zero[level][0], zero[level][1]
        if check_row(x, num) and check_col(y, num) and check_part(x, y, num):
            sudokku[x][y] = num
            bt(level + 1)
            sudokku[x][y] = 0

bt(0)
