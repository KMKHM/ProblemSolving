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
graph = [list(map(int, input().split())) for _ in range(9)]

blank = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def check_col(x, num):
    for i in range(9):
        if num == graph[x][i]:
            return False
    return True

def check_row(y, num):
    for i in range(9):
        if num == graph[i][y]:
            return False
    return True
