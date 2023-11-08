"""
색종이 붙이기
문제: https://www.acmicpc.net/problem/17136
"""
import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = 10

# 방문 여부
visited = [[0] * n for _ in range(n)]

# 색종이
board = [list(map(int, input().split())) for _ in range(n)]

# 색종이 붙일 수 있는지 판단하는 함수
def check(a, b, num):
    for i in range(a, a+num+1):
        for j in range(b, b+num+1):
            if board[i][j] != 1:
                return False
    return True


dic = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}

ans = 100

def bt(x, y, cnt):
    global ans

    if y >= 10:
        ans = min(ans, cnt)
        return

    if x >= 10:
        bt(x+1, 0, cnt)
        return

    # 0이 아닐 때
    if board[x][y]:
        for i in range(5):
            if dic[i] == 0:
                continue
            if x + i >= 10 or y + i >= 10:
                continue

            if check(x, y, i):
                for r in range(x, x+i+1):
                    for c in range(y, y+i+1):
                        board[r][c] = 0
                dic[i] -= 1
                bt(x+i+1, 0, cnt+1)
                dic[i] += 1
                for r in range(x, x+i+1):
                    for c in range(y, y+i+1):
                        board[r][c] = 1

    else:
        bt(x+1, y, cnt)

bt(0, 0, 0)

print(ans)