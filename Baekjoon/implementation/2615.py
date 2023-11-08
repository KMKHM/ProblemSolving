"""
오목
문제: https://www.acmicpc.net/problem/2615
"""
import sys

input = sys.stdin.readline

# 크기
n = 19

# 오목판
board = [list(map(int, input().split())) for _ in range(n)]

# 방향 => 오른쪽, 아래쪽, 오른쪽 대각선 아래, 오른쪽 대각선 위
dx, dy = (0, 1, 1, -1), (1, 0, 1, 1)

for x in range(n):
    for y in range(n):
        if board[x][y]:
            # 1
            # 2
            temp = board[x][y]

            # 4방향 탐색
            for k in range(4):
                # 발견한 1
                cnt = 1
                nx, ny = x + dx[k], y + dy[k]
                # 오목판안에 있을 때만
                while 0<=nx<n and 0<=ny<n:
                    # 다른 숫자나오면 break
                    if board[nx][ny] != temp:
                        break

                    cnt += 1

                    # 오목이 완성되면 육목인지 판단
                    if cnt == 5:
                        # 처음위치 전에 있는 것 확인
                        a, b = x - dx[k], y - dy[k]
                        if 0<=a<n and 0<=b<n:
                            if board[a][b] == temp:
                                break
                        #  1(1) 1(2) 1(3) 1(4) 1(5) 1
                        #   x,y                 nx, ny
                        c, d = nx + dx[k], ny + dy[k]
                        if 0<=c<n and 0<=d<n:
                            if board[c][d] == temp:
                                break
                        # 오목 완성되면 프로그램 종료
                        print(temp)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[k]
                    ny += dy[k]

print(0)
