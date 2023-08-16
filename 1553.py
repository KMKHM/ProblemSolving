"""
도미노 찾기
문제: https://www.acmicpc.net/problem/1553
"""
import sys
from collections import Counter

input = sys.stdin.readline

# 격자판 입력
board = [list(input().rstrip()) for _ in range(8)]

# 이용 가능한 숫자
nums = ["0", "1", "2", "3", "4", "5", "6"]

# 방문여부
visited = [[0]*7 for _ in range(8)]

# 가능한 조합(00~66 총 49가지)
possible = []

for i in nums:
    for j in nums:
        possible.append(i+j)

res = dict(zip(possible, [0 for _ in range(49)]))

# 가능한 조합 딕셔너리로 표현
possible = Counter(possible)


# 정답
answer = 0

# 도미노는 가로방향 또는 세로방향으로 완성할 수 있다.
dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global answer
    print(x, y)

    if res == possible:
        answer += 1


    now = board[x][y]
    visited[x][y] = 1
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < 8 and 0 <= ny < 7:
            tmp = now + board[nx][ny]
            if not visited[nx][ny]:
                if tmp in ("00", "11", "22", "33", "44", "55", "66"):
                    if res[tmp] == 0:
                        visited[nx][ny] = 1
                        res[tmp] += 1
                        dfs(nx, ny)
                        res[tmp] -= 1
                        visited[nx][ny] = 0
                else:
                    if (res[tmp] == 0) and (res[tmp[::-1]] == 0):
                        res[tmp] += 1
                        res[tmp[::-1]] += 1
                        visited[nx][ny] = 1
                        dfs(nx, ny)
                        visited[nx][ny] = 0

    visited[x][y] = 0

dfs(0, 0)

