"""
문제: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i
"""


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

        n, m = len(moveTime), len(moveTime[0])

        q = []
        visited = [[sys.maxsize] * m for _ in range(n)]

        def shortest_path(x, y):
            heapq.heappush(q, [0, x, y])
            visited[x][y] = 0

            while q:
                cur_val, curx, cury = heapq.heappop(q)
                for i in range(4):
                    nx, ny = curx + dx[i], cury + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        next_val = 0
                        if (nx, ny) == (1, 0) or (nx, ny) == (0, 1):
                            next_val = moveTime[nx][ny] + 1
                        else:
                            next_val = 1
                        val = cur_val + next_val
                        val = val if val > moveTime[nx][ny] else moveTime[nx][ny] + 1
                        if val < visited[nx][ny]:
                            visited[nx][ny] = val
                            heapq.heappush(q, [val, nx, ny])

        shortest_path(0, 0)
        return visited[n - 1][m - 1]