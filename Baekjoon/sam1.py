from collections import deque

n = 10011
# 입력할 숫자
cnt = 10011
# 층 수
part = 141

#
idx = part - 1
# 마지막 층수를 기준으로 +4 해주면 된다.
arr = [[0] * (part + idx) for _ in range(part)]

# 시작 인덱스 번호
tmp = 0

# 각 층마다 숫자가 들어갈 수 있는 마지막 인덱스
tmp2 = part + idx
for i in range(part):

    for j in range(tmp, tmp2, 2):
        arr[i][j] = cnt
        cnt -= 1
    tmp2 -= 1
    tmp += 1


dx = (1, -1, 1, -1, 0, 0)
dy = (1, -1, -1, 1, 2, -2)

visited = [[0] * (part + idx) for _ in range(part)]

s, e = 100, 1000

def bfs(x, y, target):
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = 1

    while q:
        cx, cy, c = q.popleft()
        if arr[cx][cy] == target:
            return c

        for i in range(6):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<= nx < part and 0<=ny<part+idx and not visited[nx][ny] and 0<arr[nx][ny] <= 10000:
                visited[nx][ny] = 1
                q.append([nx, ny, c+1])

for i in range(part):
    for j in range(part+idx):
        if arr[i][j] == s:
            print(bfs(i, j, e))