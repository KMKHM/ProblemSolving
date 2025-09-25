class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        n = len(triangle)

        for i in range(1, n):
            m = len(triangle[i])
            for j in range(m):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == m - 1:
                    triangle[i][j] += triangle[i - 1][-1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

        return min(triangle[n - 1])