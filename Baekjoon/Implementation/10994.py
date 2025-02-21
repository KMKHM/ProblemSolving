"""
별 찍기 - 19
문제: https://www.acmicpc.net/problem/10994
"""
n = int(input())

# 사각형의 크기
size = 4*n - 3

board = [[" "] * size for _ in range(size)]

if n == 1:
    print("*")
else:
    init, temp_size = 0, 4 * n - 3
    while 1:
        # 테두리만 채워주기
        for i in range(init, init + temp_size):
            board[init][i] = "*"
            board[init + temp_size - 1][i] = "*"
            board[i][init] = "*"
            board[i][init + temp_size - 1] = "*"
        n -= 1
        temp_size = 4 * n - 3
        init += 2
        if n == 0:
            break

    for i in range(size):
        for j in range(size):
            print(board[i][j], end="")
        print()