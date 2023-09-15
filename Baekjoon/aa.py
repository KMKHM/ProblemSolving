import sys
sys.setrecursionlimit(10**8)


n, m = 3, 4
x, y = 2, 3
r, c = 3, 1
k = 5
# 4 방향
directions = ['d', 'l', 'r', 'u']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

answer = ""

visited = [[0]*(m+1) for _ in range(n+1)]
res = []
flag = False
def dfs(start1, start2, end1, end2, cnt, way):
    global answer, flag

    if flag:
        return

    if abs(start1-end1) + abs(start2-end2) + cnt > k:
        return

    if cnt > k:
        return

    if not flag and cnt == k:
        if start1 == end1 and start2 == end2:
            flag = True
            answer = way
            return


    if start1 == end1 and start2 == end2 and cnt == k:
        res.append(way)
        return

    for i in range(4):
        nx, ny = start1 + dx[i], start2 + dy[i]
        if 1<=start1<=n and 1<=start2<=m:
            dfs(nx, ny, end1, end2, cnt + 1, way+directions[i])





dfs(x, y, r, c, 0, "")

print(answer)
