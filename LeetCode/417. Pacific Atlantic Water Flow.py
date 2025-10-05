class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        n, m = len(heights), len(heights[0])

        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

        def bfs(x, y):
            flag1, flag2 = False, False
            visited = [[0] * m for _ in range(n)]
            q = deque()
            q.append([x, y])
            visited[x][y] = 1

            while q:
                curx, cury = q.popleft()
                if curx == 0 or cury == 0:
                    flag1 = True
                if curx == n - 1 or cury == m - 1:
                    flag2 = True
                if flag1 and flag2:
                    return True
                for i in range(4):
                    nx, ny = curx + dx[i], cury + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and heights[nx][ny] <= heights[curx][cury]:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
            return False

        res = []

        for i in range(n):
            for j in range(m):
                if bfs(i, j):
                    res.append([i, j])
        return res