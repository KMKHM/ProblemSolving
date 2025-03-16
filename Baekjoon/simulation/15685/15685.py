import sys

input = sys.stdin.readline

direction = {0: [0, 1],  # →
             1: [-1, 0], # ↑
             2: [0, -1], # ←
             3: [1, 0]}  # ↓

# 드래곤 커브 저장할 격자판
board = [[0]*101 for _ in range(101)]

# 드래곤 커브 그리기 함수
def curve(x, y, d, g):
    # 방향 리스트
    dirs = [d]

    # 이전 세대의 방향을 이용해 새로운 방향 생성
    for _ in range(g):
        new_dirs = [(d + 1) % 4 for d in reversed(dirs)]
        dirs += new_dirs

    # 커브를 따라 격자에 표시
    board[y][x] = 1  # 시작점
    for d in dirs:
        x, y = x + direction[d][0], y + direction[d][1]
        board[y][x] = 1

# 입력 처리
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 각 드래곤 커브 적용
for x, y, d, g in arr:
    x, y = y, x
    curve(x, y, d, g)

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

# 정답 출력
print(result)
